"""ミノ駆動本読書py"""
from dataclasses import dataclass
from datetime import time


@dataclass
class MinoDrivenBookReadingPy:
    count: int
    connpass_url: str
    reading_range: str
    start_time: str
    main_time: str
    reading_book_time: str
    chapter: list

    def make_message(self):
        title = self._title()
        tag = self._tag()
        please = self._please()
        what_is_this_memo = self._what_is_this_memo()
        flow = self._flow()
        chapter = self._make_chapter()
        return title + tag + please + what_is_this_memo + flow + chapter

    def _title(self):
        return f"# (template) ミノ駆動本_読書py[{self.count}] みんなのメモ\n\n"

    def _tag(self):
        return "###### tags: `ミノ駆動本`\n\n" \
               "- このメモはWebに公開されています（HackMDチーム）\n" \
               "- リンクを知っている人は見られます\n" \
               "- HackMDにログインして編集できます\n\n"

    def _please(self):
        return "## お願い事項\n\n" \
               "https://twitter.com/MinoDriven/status/1541334416622256130\n\n" \
               "> 【お願い】" \
               "拙著『良いコード／悪いコードで学ぶ設計入門』に関する情報発信について。\n" \
               "ブログ等で発信の際は、引用の範囲を超え、著作権侵害となる場合は勿論のこと、" \
               "拙著の詳細内容が分かるような表現での公開はお控え頂けると助かります。" \
               "ご感想や拙著に基づく試行錯誤は歓迎です。 #ミノ駆動本\n\n" \
               "とミノ駆動さんが仰られていますので、勉強会そのものでも詳細内容がわかる記述はしないように気をつけていきましょう。\n\n"

    def _what_is_this_memo(self):
        return "## このメモについて\n\n" \
               f"このメモは ミノ駆動本_読書py[{self.count}] のメモです\n" \
               f"{self.connpass_url}\n\n" \
               f"読む範囲: {self.reading_range}\n\n" \
               "ミノ駆動本のサポートページより、Javaのサンプルコードが見られます。\n" \
               "https://gihyo.jp/book/2022/978-4-297-12783-1/support\n\n"

    def _flow(self):
        return "## 読書会の流れ\n\n" \
               f"* {self.mokumoku_timreading_book_time} **自由参加**のもくもく会（個人作業）\n" \
               "- 事前に読む時間がとれなかった方はここで読んじゃいましょう（ざっとで大丈夫です）\n" \
               "- 合わせて、この**HackMD**に話したいことを各自書いてください\n" \
               "        - ログインすれば書ける設定にしています\n" \
               "        - ここがわからん、ここはわかった　お気軽に書き込んでみてください\n" \
               "        - HackMDの書き込みに投票し、みんなが気になるところをわいわい読み解いていきます\n" \
               f"* {self.main_time} 読書会本編（みんなでわいわい）\n" \
               "    * Discordでスライド共有して別途案内します\n" \
               f"    * {self.start_time}時開始の本編では、「わたしこれ気になる！」" \
               f"という話題に `:+1:` と書いて投票します。\n" \
               "        * :+1: する上限はありません。" \
               "気になる話題に全部 :+1: しちゃいましょう。" \
               "ただし1つの話題には1個だけ:+1:でお願いします\n" \
               "    * 票数が多い話題から話していきます。\n\n"

    def _mokumoku_workzone(self):
        return "## 以下、もくもく会ワークゾーン\n\n" \
               "### 感想、気付き\n\n" \
               "- \n" \
               "- \n" \
               "- \n"

    def _kininaru(self, *args):
        return "以下は各節で「これってどういうことなんだろう」" \
               "「ここからこういう気付きがあった」などを書き出すゾーンです。" \
               f"{self.reading_range}章"

    def _make_chapter(self):
        tmp = ''
        count = 0
        for i in self.chapter:
            if count == 0:
                t = f"### {i}\n\n"
                tmp += t
                count += 1
                continue
            t = f"#### {i}\n\n" \
                "- \n" \
                "- \n" \
                "- \n\n"
            tmp += t
        return tmp

    def _calc_datetime(self):
        default_time = 20
        default_minute = 00
        self.start_time
        print(time(hour=20, minute=00).isoformat(timespec='minutes'))


if __name__ == '__main__':
    # チャプターは以下のシートを流用するとサクッと作れるようにしています
    # https://docs.google.com/spreadsheets/d/1dleM32o2iy5_QgGx9U7Ku9NGiGky7ZX0EinWDXNfi8g/edit#gid=0
    mino_driven = MinoDrivenBookReadingPy(
        count=6,
        connpass_url="https://pythonista-books.connpass.com/event/256267/",
        reading_range="10章",
        start_time="20",
        reading_book_time="19:30〜20:00",
        main_time="20:00〜21:30",
        chapter=[
            '10 名前設計 ―あるべき構造を見破る名前―',
            '10.1 悪魔を呼び寄せる名前',
            '10.2 名前を設計する―目的駆動名前設計',
            '10.3 設計時の注意すべきリスク',
            '10.4 意図がわからない名前',
            'Column 技術駆動命名を用いる分野もある',
            '10.5 構造を大きく歪ませてしまう名前',
            'Column クソコード動画「Managerクラス」',
            '10.6 名前的に居場所が不自然なメソッド',
            '10.7 名前の省略',
        ]
    )
    print(mino_driven.make_message())