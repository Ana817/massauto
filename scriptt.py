import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
