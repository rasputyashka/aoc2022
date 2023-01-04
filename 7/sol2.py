from __future__ import annotations

from dataclasses import dataclass, field

CONSTANT_MAX = 100000


@dataclass
class FileObject:
    name: str
    size: int


@dataclass
class DirectoryObject:
    name: str
    subfolders: dict[DirectoryObject] = field(default_factory=dict)
    files: list[FileObject] = field(default_factory=list)
    parent: str | None = None
    size: int = 0

    def add_file(self, file):
        self.files.append(file)
        self.size += file.size
        parent = self.parent
        while parent is not None:
            parent.size += file.size
            parent = parent.parent


def process_ls(current_dir, dir_data):
    for line in dir_data:
        line_data = line.split()
        match line_data:
            case ["dir", dir_name]:
                current_dir.subfolders[dir_name] = DirectoryObject(
                    dir_name, parent=cur_dir
                )
            case [file_size, filename]:
                file = FileObject(filename, int(file_size))
                current_dir.add_file(file)


def solve(dir_object, cur_min):
    for directory in dir_object.subfolders.values():
        cur_min = solve(directory, cur_min)
    if SPACE_NEEDED <= dir_object.size <= cur_min:
        return dir_object.size
    return cur_min


root = DirectoryObject("/")
cur_dir = root

ls_info = []
ls_active = False
for line in open(0):
    line = line.strip()
    if line.startswith("$ cd"):
        if ls_active:
            process_ls(cur_dir, ls_info)
            ls_info.clear()
            ls_active = False
        target_dir = line.removeprefix("$ cd ")
        if target_dir == "/":
            cur_dir = root
        elif target_dir == "..":
            cur_dir = cur_dir.parent
        else:
            cur_dir = cur_dir.subfolders[target_dir]
    elif line == "$ ls":
        ls_active = True
    else:
        if ls_active:
            ls_info.append(line)
else:
    # handle last `ls`
    process_ls(cur_dir, ls_info)

if __name__ == "__main__":
    disk_space = 70000000
    SPACE_NEEDED = 30000000 - (disk_space - root.size)
    print(solve(root, root.size))
