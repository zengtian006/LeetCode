class File:
    def __init__(self):
        self.child = collections.defaultdict(File)
        self.isFile = False
        self.content = ""
        self.name = ""


class FileSystem:

    def __init__(self):
        self.root = File()    
    
    def ls(self, path: str) -> List[str]:
        res = []
        path = path.split('/')[1:]
        cur = self.root
        if path[0]!='':
            for p in path:
                cur = cur.child[p]
        if cur.isFile:
            return [cur.name]
        for ch in cur.child:
            res.append(ch)
        return sorted(res)

    def mkdir(self, path: str) -> None:
        cur = self.root
        paths = path.split('/')[1:]
        for p in paths:
            cur = cur.child[p]
            cur.name = p

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur =self.root
        filePath = filePath.split('/')[1:]
        for p in filePath:
            cur = cur.child[p]
            cur.name = p
        cur.isFile = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur =self.root
        filePath = filePath.split('/')[1:]
        for p in filePath:
            cur = cur.child[p]
        if cur.isFile:
            return cur.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)