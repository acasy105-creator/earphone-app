import streamlit as st

# 1. データの準備
earphone_list = [
    # 🎮 ゲーム中心
    {"useCase": "ゲーム中心", "focus": "迫力の重低音", "shape": "完全ワイヤレス", "budget": "5,000円以下", "name": "Anker Soundcore P31i", "price": "約4,990円", "reason": "5000円以下なのにアンカー特有のズンと響く重低音が楽しめる！爆発音などの迫力が段違いで、コスパ良くゲーム環境を上げたい人に最適。", "url": "https://www.amazon.co.jp/dp/dummy1"},
    {"useCase": "ゲーム中心", "focus": "迫力の重低音", "shape": "遅延のない有線", "budget": "1万円以下", "name": "Sennheiser IE 200", "price": "約9,800円", "reason": "有線だから音ズレ完全ゼロ。セールで1万円を切る破格ながら、深みのある低音でRPGの世界観やアクションの迫力にどっぷり浸れるよ！", "url": "https://www.amazon.co.jp/dp/dummy2"},
    {"useCase": "ゲーム中心", "focus": "クリアな高音・ボーカル", "shape": "遅延のない有線", "budget": "5,000円以下", "name": "AZLA ASE-500", "price": "約2,000円", "reason": "有線で遅延ゼロ。足音やリロード音がくっきり聞こえるから、FPSで「音の方向がわかる」という圧倒的有利な状況をこの安さで体験できる！", "url": "https://www.amazon.co.jp/dp/dummy3"},
    {"useCase": "ゲーム中心", "focus": "クリアな高音・ボーカル", "shape": "遅延のない有線", "budget": "1万円以下", "name": "Sennheiser IE 100 PRO", "price": "約9,600円", "reason": "プロも愛用するモニターイヤホン。余計な低音の響きがなく、壁越しの足音の方向と距離が恐ろしいほど正確に把握できるため、撃ち合いの勝率アップに直結するよ！", "url": "https://www.amazon.co.jp/dp/dummy4"},
    {"useCase": "ゲーム中心", "focus": "マイク性能", "shape": "遅延のない有線", "budget": "1万円以下", "name": "TRN Conch", "price": "約4,680円", "reason": "マイク付きケーブルも選べる中華イヤホンの傑作。遅延ゼロで味方との連携も完璧。価格バグレベルの解像度で足音もバッチリ聞こえるよ。", "url": "https://www.amazon.co.jp/dp/dummy5"},
    {"useCase": "ゲーム中心", "focus": "マイク性能", "shape": "完全ワイヤレス", "budget": "予算は気にしない", "name": "JBL Tour Pro 3", "price": "約30,000円", "reason": "ワイヤレスなのに付属ケースをPCに挿すだけで「遅延ゼロ」になる神機能搭載！味方とのボイチャも極めてクリアで、ゲーム環境の最終形態と言えるデバイス。", "url": "https://www.amazon.co.jp/dp/dummy6"},
    {"useCase": "ゲーム中心", "focus": "長時間つけても疲れない装着感", "shape": "耳を塞がないイヤカフ型", "budget": "1万円以下", "name": "EarFun Clip", "price": "約6,990円", "reason": "耳に挟むだけだから、休日に1日中ゲームをしていても全く耳が痛くならない。実家暮らしにも超おすすめ！", "url": "https://www.amazon.co.jp/dp/dummy7"},
    {"useCase": "ゲーム中心", "focus": "長時間つけても疲れない装着感", "shape": "没入感のあるヘッドホン", "budget": "3万円以下", "name": "Sennheiser HD 599 SE", "price": "約12,800円", "reason": "開放型ヘッドホンならではの「音の抜け」が最強。耳を圧迫しないベロア素材のパッドで、長時間のPCゲームでも全く蒸れずに快適なプレイ環境を作れるよ。", "url": "https://www.amazon.co.jp/dp/dummy8"},
    {"useCase": "ゲーム中心", "focus": "迫力の重低音", "shape": "完全ワイヤレス", "budget": "1万円以下", "name": "Anker Soundcore P40i", "price": "約6,990円", "reason": "迫力の重低音でゲームの没入感を底上げ。さらにケースがスマホスタンドになるから、攻略動画を見ながらのプレイにもめちゃくちゃ便利！", "url": "https://www.amazon.co.jp/dp/dummy9"},

    # 🎵 音楽中心
    {"useCase": "音楽中心", "focus": "迫力の重低音", "shape": "完全ワイヤレス", "budget": "1万円以下", "name": "EarFun Air Pro 4", "price": "約7,990円", "reason": "ハイレゾ対応、強力ノイキャン、ワイヤレス充電など欲しい機能が全部入り。ロックやEDMのビートが最高に気持ちよく響く、1万円以下の絶対的王者。", "url": "https://www.amazon.co.jp/dp/dummy10"},
    {"useCase": "音楽中心", "focus": "迫力の重低音", "shape": "没入感のあるヘッドホン", "budget": "1万円以下", "name": "Anker Soundcore Space Q45", "price": "約9,990円", "reason": "ヘッドホンならではの圧倒的な重低音とハイレゾ対応。ライブハウスの最前列にいるような迫力を、強力なノイズキャンセリング空間で独り占めできるよ。", "url": "https://www.amazon.co.jp/dp/dummy11"},
    {"useCase": "音楽中心", "focus": "迫力の重低音", "shape": "完全ワイヤレス", "budget": "3万円以下", "name": "JBL Tour Pro 2", "price": "約21,000円", "reason": "エンタメ界の巨匠JBLならではの、躍動感あふれる重低音。ケースの液晶画面でスマートに操作するガジェットとしての楽しさも満載！", "url": "https://www.amazon.co.jp/dp/dummy12"},
    {"useCase": "音楽中心", "focus": "クリアな高音・ボーカル", "shape": "完全ワイヤレス", "budget": "1万円以下", "name": "AVIOT TE-Upn", "price": "約8,173円", "reason": "プロドラマー監修で、ボーカルの息遣いまで鮮やかに楽しめる。3つの音質モード切り替えで、どんな曲も最高のコンディションで聴けるよ。", "url": "https://www.amazon.co.jp/dp/dummy13"},
    {"useCase": "音楽中心", "focus": "クリアな高音・ボーカル", "shape": "完全ワイヤレス", "budget": "3万円以下", "name": "Sennheiser Momentum True Wireless 4", "price": "約27,900円", "reason": "繊細な高音とバランスの取れた音作り。ジャズからポップスまで、アーティストの声を美しく鳴らし切るハイエンドの圧倒的な実力。", "url": "https://www.amazon.co.jp/dp/dummy14"},
    {"useCase": "音楽中心", "focus": "クリアな高音・ボーカル", "shape": "完全ワイヤレス", "budget": "予算は気にしない", "name": "Technics EAH-AZ100", "price": "約35,000円", "reason": "総合力No.1！原音に忠実で解像度の高い極上のサウンド。ジャンルを選ばず、すべての音楽を一段階上の感動に引き上げる至高の1台だよ。", "url": "https://www.amazon.co.jp/dp/dummy15"},
    {"useCase": "音楽中心", "focus": "マイク性能", "shape": "完全ワイヤレス", "budget": "5,000円以下", "name": "Xiaomi Redmi Buds 6 Lite", "price": "約2,480円", "reason": "この圧倒的な安さでノイキャンも専用アプリもマイク機能まで実用的。通勤・通学の音楽用とちょっとした通話用に、とりあえず買うならコレ！", "url": "https://www.amazon.co.jp/dp/dummy16"},
    {"useCase": "音楽中心", "focus": "長時間つけても疲れない装着感", "shape": "耳を塞がないイヤカフ型", "budget": "3万円以下", "name": "Shokz Open Dots 1", "price": "約22,000円", "reason": "オープンイヤー型なのに低音がしっかり出る驚きの音質。1日中つけていても全く耳が痛くならない至高の快適さで、音楽が日常に溶け込むよ。", "url": "https://www.amazon.co.jp/dp/dummy17"},
    {"useCase": "音楽中心", "focus": "長時間つけても疲れない装着感", "shape": "完全ワイヤレス", "budget": "予算は気にしない", "name": "Denon PerL Pro", "price": "約22,000円", "reason": "自動であなたの耳の形をスキャンし、あなただけの専用の音を作ってくれる魔法の「パーソナライズ機能」搭載。長時間のリスニングが最高の贅沢に変わる！", "url": "https://www.amazon.co.jp/dp/dummy18"},

    # 💼 仕事・通話
    {"useCase": "仕事・通話", "focus": "マイク性能", "shape": "完全ワイヤレス", "budget": "1万円以下", "name": "Anker Soundcore P40i", "price": "約6,990円", "reason": "クリアな通話品質と強力なノイズキャンセリング。カフェでの作業中も周囲の雑音を消し去り、自分の声だけを相手にしっかり届けてくれるよ。", "url": "https://www.amazon.co.jp/dp/dummy19"},
    {"useCase": "仕事・通話", "focus": "マイク性能", "shape": "耳を塞がないイヤカフ型", "budget": "3万円以下", "name": "Shokz OpenComm 2", "price": "約19,000円", "reason": "口元にマイクが伸びているため、キーボードのタイピング音をカットして自分の声だけを相手に届ける。長時間のWEB会議に必須の最強ビジネスギア！", "url": "https://www.amazon.co.jp/dp/dummy20"},
    {"useCase": "仕事・通話", "focus": "マイク性能", "shape": "完全ワイヤレス", "budget": "予算は気にしない", "name": "Apple AirPods Pro (第3世代)", "price": "約39,800円", "reason": "iPhoneやMacとの切り替えが全自動でシームレス。通話品質も最高レベルで、Appleデバイス環境ならこれ以上の仕事効率化アイテムはないよ。", "url": "https://www.amazon.co.jp/dp/dummy21"},
    {"useCase": "仕事・通話", "focus": "長時間つけても疲れない装着感", "shape": "耳を塞がないイヤカフ型", "budget": "1万円以下", "name": "SoundPEATS GoFree 2", "price": "約7,581円", "reason": "PCとスマホ両方に同時接続できるマルチポイント対応。耳を塞がないから長時間のデスクワークでも疲れず、同僚から話しかけられてもすぐ反応できる！", "url": "https://www.amazon.co.jp/dp/dummy22"},
    {"useCase": "仕事・通話", "focus": "長時間つけても疲れない装着感", "shape": "完全ワイヤレス", "budget": "1万円以下", "name": "Sony WF-C510", "price": "約9,000円", "reason": "非常にコンパクトで耳への圧迫感がゼロ。外音取り込み機能が優秀で、オフィスでBGMを流しつつ周囲の音も自然に聞こえる便利な相棒だよ。", "url": "https://www.amazon.co.jp/dp/dummy23"},
    {"useCase": "仕事・通話", "focus": "クリアな高音・ボーカル", "shape": "遅延のない有線", "budget": "5,000円以下", "name": "AZLA ASE-500", "price": "約2,000円", "reason": "有線でUSB-C直結のため、WEB会議中の声の途切れやバッテリー切れの心配がゼロ。相手の声をくっきり聴き取れる、仕事用の頼れるサブ機として最適。", "url": "https://www.amazon.co.jp/dp/dummy24"},
    {"useCase": "仕事・通話", "focus": "長時間つけても疲れない装着感", "shape": "没入感のあるヘッドホン", "budget": "1万円以下", "name": "AVIOT WA-V1", "price": "約9,990円", "reason": "120時間というバグレベルのバッテリー持ち。充電の手間がなく、アルミを使った美しいデザインでWEB会議でもスタイリッシュな印象を与えられるよ。", "url": "https://www.amazon.co.jp/dp/dummy25"},
    {"useCase": "仕事・通話", "focus": "マイク性能", "shape": "完全ワイヤレス", "budget": "3万円以下", "name": "Anker Soundcore Liberty 4 Pro", "price": "約13,990円", "reason": "アンカー最上位の高品質な通話ノイズリダクション。AirPodsライクな「つまんで操作」でミュートなどの操作も確実に行えるプロフェッショナル仕様。", "url": "https://www.amazon.co.jp/dp/dummy26"},

    # 💼 動画・ASMR
    {"useCase": "動画・ASMR", "focus": "クリアな高音・ボーカル", "shape": "遅延のない有線", "budget": "5,000円以下", "name": "final E500", "price": "約1,000円台", "reason": "ASMRを聴くために開発された専用イヤホン。耳元で囁かれる息遣いや耳かきのゾクゾク感が、他のイヤホンとは次元が違う圧倒的な生々しさ！", "url": "https://www.amazon.co.jp/dp/dummy27"},
    {"useCase": "動画・ASMR", "focus": "迫力の重低音", "shape": "完全ワイヤレス", "budget": "3万円以下", "name": "Bose QuietComfort Ultra", "price": "約39,000円", "reason": "シネマモード搭載で空間オーディオの出来が秀逸。圧倒的なノイキャン空間の中で、映画館のど真ん中にいるような極上の映像体験ができるよ。", "url": "https://www.amazon.co.jp/dp/dummy28"},
    {"useCase": "動画・ASMR", "focus": "長時間つけても疲れない装着感", "shape": "完全ワイヤレス", "budget": "1万円以下", "name": "Sony WF-C510", "price": "約9,000円", "reason": "めちゃくちゃ小さくて軽いから、ベッドで寝転がりながら使っても耳への圧迫感が少ない。寝る前の長時間の動画視聴にぴったりの癒しイヤホン。", "url": "https://www.amazon.co.jp/dp/dummy29"},
    {"useCase": "動画・ASMR", "focus": "長時間つけても疲れない装着感", "shape": "没入感のあるヘッドホン", "budget": "3万円以下", "name": "Sennheiser HD 599 SE", "price": "約12,800円", "reason": "開放型ならではの音の広がり。自宅のソファでリラックスしながら、長時間のライブ映像や映画を大迫力・大空間で楽しむなら至高の選択肢！", "url": "https://www.amazon.co.jp/dp/dummy30"},
    {"useCase": "動画・ASMR", "focus": "クリアな高音・ボーカル", "shape": "完全ワイヤレス", "budget": "予算は気にしない", "name": "Apple AirPods Pro (第3世代)", "price": "約39,800円", "reason": "空間オーディオの「顔の向きに音が追従する機能」が魔法のように自然。iPadやiPhoneでの動画視聴が、まるで現実の空間に音が配置されている感覚になるよ。", "url": "https://www.amazon.co.jp/dp/dummy31"},
    {"useCase": "動画・ASMR", "focus": "迫力の重低音", "shape": "完全ワイヤレス", "budget": "1万円以下", "name": "AVIOT TE-Upn", "price": "約8,173円", "reason": "グルーブモードに変更すれば、映画の爆発音やライブ映像の地鳴りのような低音をフルパワーで体感できる。映像の迫力を120%引き出すならコレ！", "url": "https://www.amazon.co.jp/dp/dummy32"},
    {"useCase": "動画・ASMR", "focus": "長時間つけても疲れない装着感", "shape": "耳を塞がないイヤカフ型", "budget": "1万円以下", "name": "EarFun Clip", "price": "約6,990円", "reason": "耳をふさがないので、休日にゴロゴロしながらYouTubeを流し見していても全くストレスがない。着けているのを忘れるくらい快適な視聴環境が作れるよ。", "url": "https://www.amazon.co.jp/dp/dummy33"},
    {"useCase": "動画・ASMR", "focus": "クリアな高音・ボーカル", "shape": "遅延のない有線", "budget": "1万円以下", "name": "Sennheiser IE 200", "price": "約9,800円", "reason": "有線だから映像と音のズレが完全ゼロ。ボーカルの息遣いやセリフが恐ろしいほどクリアに聞こえるため、ドラマや映画の世界観に深く補入できる！", "url": "https://www.amazon.co.jp/dp/dummy34"}
]
# ※動作確認のため4つだけ入れています。後で自由に追加できます！

# 2. 画面のUI
st.title("🎧 最適イヤホン診断ツール")
st.write("4つの質問に答えるだけで、あなたにぴったりのデバイスを導き出します。")

ans1 = st.radio("Q1：主な用途は？", ["ゲーム中心", "音楽中心", "仕事・通話", "動画・ASMR"])
ans2 = st.radio("Q2：一番こだわるポイントは？", ["迫力の重低音", "クリアな高音・ボーカル", "マイク性能", "長時間つけても疲れない装着感"])
ans3 = st.radio("Q3：好きなタイプ（形状）は？", ["完全ワイヤレス", "耳を塞がないイヤカフ型", "遅延のない有線", "没入感のあるヘッドホン"])
ans4 = st.radio("Q4：予算は？", ["5,000円以下", "1万円以下", "3万円以下", "予算は気にしない"])

# 3. 診断ロジック
if st.button("診断結果を見る", type="primary"):
    best_match = earphone_list[0]
    max_score = -1

    for earphone in earphone_list:
        score = 0
        if earphone["useCase"] == ans1: score += 1
        if earphone["focus"] == ans2: score += 1
        if earphone["shape"] == ans3: score += 1
        if earphone["budget"] == ans4: score += 1
        
        if score > max_score:
            max_score = score
            best_match = earphone

    # 4. 結果の表示
    st.divider()
    st.subheader("あなたに最適なデバイスは…")
    st.header(best_match["name"])
    st.success(best_match["price"])
    st.write(best_match["reason"])
    st.link_button("Amazonで詳細を見る", best_match["url"])