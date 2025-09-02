# target_colを指定する
npt = nlplot.NLPlot(df, target_col='words')

# top_nで頻出上位単語, min_freqで頻出下位単語を指定できる
stopwords = npt.get_stopword(top_n=0, min_freq=0)

#単語頻出ランキングを作成
fig_unigram = npt.bar_ngram(
    title='uni-gram',
    xaxis_label='word_count',
    yaxis_label='word',
    ngram=1,
    top_n=50,
    stopwords=stopwords,
)
#単語頻出ランキングを表示
fig_unigram.show()
# # うまく表示されない場合はファイルに保存する
# fig_unigram.write_html("unigram.html")