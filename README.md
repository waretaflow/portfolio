# 僕のサイト

## 主な機能
- トップページ
    - 最新トピックとか
    - 連絡先
- 経歴
    - 学歴
    - 職歴
- カレンダー
    - 予定をリアルタイムで更新
    - zoomで相談とか受ける

# Vue.jsの開発で大事そうなメモ
- Vueオブジェクトのプロパティは、初期化時に存在していたもののみ、変更と同時に再レンダリンが行われる
    - 後から追加された(初期化時に存在しなかった)プロパティが更新されてもレンダリングは行われない
    - 例外的に、`Object.freeze(obj)`を利用すると、そのオブジェの更新では再レンダリングされなくなる
- DjangoにVue.jsを組み込むときの方法は大きく分けて二種類か
    - Vue.jsからhttpリクエスト送って、DjangoをAPIとして運用する方法
    - DjangoのtemplateにCDNでVueを組み込む
- HTTPリクエストはaxiosで送る