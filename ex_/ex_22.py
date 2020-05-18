"""
TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，
你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。

"""

import base64


class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        c = base64.encodebytes(longUrl)
        return c

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        d = base64.decodebytes(shortUrl)
        return d


# Your Codec object will be instantiated and called as such:
url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
z = codec.decode(codec.encode(url))
print(z)
