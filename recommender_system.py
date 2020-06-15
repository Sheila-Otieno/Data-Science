import pandas as pd
import warnings 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from numpy.linalg import svd

warnings.filterwarnings('ignore')
games = pd.read_csv("googleplaystore.csv")
#print(games.head())
print(games.info())
print(games.shape)

#removing missing values
total = games.isnull().sum().sort_values(ascending=False)
percent = (games.isnull().sum()/games.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total,percent],axis=1,keys=['Total','Percent'])
print(missing_data.head())

games.dropna(how='any',inplace=True)

total = games.isnull().sum().sort_values(ascending=False)
percent = (games.isnull().sum()/games.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(missing_data.head())

print(games.shape)
print(games['Rating'].describe())

C=games['Rating'].mean()
print(C)
games['Reviews']=games['Reviews'].astype(float)
m = games['Reviews'].quantile(0.75)
print(m)

p_games = games.copy().loc[games['Reviews'] >= m]
print(p_games.shape)

def get_weighted_rating(x, m=m,C=C):
    v = x['Rating']
    R = x['Reviews']
    return (v/(v+m)* R) + (m/(m+v) * C)

p_games['score'] = p_games.apply(get_weighted_rating,axis=1)
p_games = p_games.sort_values('score',ascending=False)
print(p_games[['App','Category','Rating','Reviews','score']].head(15))
print(games['Category'].head())
print(games['Category'].describe())

#construct the TFID matrix
tfidf= TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(games['Category'])
print(tfidf_matrix.shape)

#cosine similarity
cosine_similarity = linear_kernel(tfidf_matrix,tfidf_matrix)
indices = pd.Series(games.index, index=games['App']).drop_duplicates()

def getrecommendations(title,cosine_similarity=cosine_similarity):
    idx=indices[title]
    sim_scores=list(enumerate(cosine_similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1],reverse=any(True))
    sim_scores = sim_scores[1:11]
    app_indices = [i[0] for i in sim_scores]
    return games['App'].iloc[app_indices]


#print(getrecommendations('Sketch - Draw & Paint'))
#print("Item 2")
#print(getrecommendations('ibis Paint X'))
print("Item 3")
#print(getrecommendations('GO SMS Pro - Messenger, Free Themes, Emoji'))
#print("Item 4")
#print(getrecommendations('Zombie Catchers'))

def new_recommendations(appname):
    idx = indices[appname]
    sim_scores = list(enumerate(cosine_similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    app_indices = [i[0] for i in sim_scores]

    apps= p_games.iloc[app_indices][['App','Category','Rating','Reviews','Genres']]
    ratings=apps[apps['Rating'].notnull()]['Rating'].astype('int')
    reviews=apps[apps['Reviews'].notnull()]['Reviews'].astype('int')
    #C=ratings.mean()
    m=reviews.quantile(0.60)
    qualified= apps[(apps['Reviews']>=m) & (apps['Reviews'].notnull()) & (apps['Rating'].notnull())]
    qualified['Reviews']=qualified['Reviews'].astype('int')
    qualified['Rating'] = qualified['Rating'].astype('int')
    qualified['wr'] = qualified.apply(get_weighted_rating, axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(10)
    return qualified

print('Improved recommendation')
print('#1')
#print(new_recommendations('FlipaClip - Cartoon animation'))
print('#2')
#print(new_recommendations('Voxel - 3D Color by Number & Pixel Coloring Book'))
#print('#3')
#print(new_recommendations('Instagram'))

#def app_recommendations(appname):
#idx = indices[appname]
#sim_scores = list(enumerate(cosine_similarity[idx]))
#sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#sim_scores = sim_scores[1:11]
#app_indices = [i[0] for i in sim_scores]
#return games.iloc[app_indices]


#print('#1: FlipaClip - Cartoon animation')
#print(app_recommendations('FlipaClip - Cartoon animation'))
#print('#2: Wipe out')
#print(app_recommendations('Wipe out'))


user_reviews = pd.read_csv("googleplaystore_user_reviews.csv")
#print(user_reviews.head())
#removing missing values
total = user_reviews.isnull().sum().sort_values(ascending=False)
percent = (user_reviews.isnull().sum()/user_reviews.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(missing_data.head())

user_reviews.dropna(how='any', inplace=True)

total = user_reviews.isnull().sum().sort_values(ascending=False)
percent = (user_reviews.isnull().sum()/user_reviews.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(missing_data.head())

print(user_reviews.head())

def main():
    app= input('Enter the app name:')
    app= str(app)
    print('Recommendations for ', app)
    new_recommendations(app)

main()


#hybrid recommender system


def hybrid(category_num, appname):
    index = indices[appname]
    tmdbId = games.loc[appname]['Category_c']
    app_id = games.loc[appname]['Category_c']

    sim_scores = list(enumerate(cosine_similarity[int(index)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    game_indices = [i[0] for i in sim_scores]

    apps = games.iloc[game_indices][['App', 'Rating',
                                     'Review', 'Category', 'Content Rating']]
    apps['est'] = apps['Category_c'].apply(lambda x: svd.predict(
        category_num, game_indices.loc[x]['Category_c']).est)
    apps = apps.sort_values('est', ascending=False)
    return apps.head(10)


#print(hybrid(18, 'Photo Editor & Candy Camera & Grid & ScrapBook'))

#print(user_reviews.head())
user_reader = Reader()
review = Dataset.load_from_df(
    user_reviews[['App', 'Sentiment_Polarity', 'Sentiment_Subjectivity']], user_reader)
review.split(n_folds=4)
svd = SVD()
#print(evaluate(svd, review, measures=['RMSE', 'MAE']))
