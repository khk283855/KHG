from prediction_util import PredictionUtil

gildong = PredictionUtil()

gildong.read('score.csv')
gildong.boxplot('score1','score2')
gildong.lmplot('score1','score2','score3')
gildong.plot_3d('score1','score2','score3')
gildong.heatmap(['score1','score2','score3','avg','grade'])
gildong.run_all(['score1','score2','score3','avg'], 'grade')