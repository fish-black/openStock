class StrUtil:

    def is_chuang_ye_ban(self, code):
        return code.startswith("sz.3") > 0 or code.startswith("sh.3") > 0

    def is_shen_zhen(self, code):
        return code.startswith("sz.0") > 0 or code.startswith("sh.0") > 0

    def is_shang_zheng(self, code):
        return code.startswith("sz.6") > 0 or code.startswith("sh.6") > 0
