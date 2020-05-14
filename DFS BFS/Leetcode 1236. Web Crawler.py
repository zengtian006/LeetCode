class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl[:startUrl.find('/', startUrl.find('//')+2)]
        q = collections.deque()
        q.append(startUrl)
        res = [startUrl]
        visited = set()
        visited.add(startUrl)
        while q:
            url = q.popleft()
            urls = htmlParser.getUrls(url)
            for u in urls:
                if u.find(hostname)>=0 and u not in visited:
                    visited.add(u)
                    res.append(u)
                    q.append(u)
        return res