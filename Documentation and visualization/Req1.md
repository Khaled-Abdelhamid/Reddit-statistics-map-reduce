[TOC]



# Algorithm

1. We need to filter the data first based on the top subreddits , hence we will have to rank and sort all the subreddits that exists in the dataset to get the top `X` values.
2. we need to know some way to get all the topics that have been said per  user and per subreddit.
3. for all these topics ,  we need a consistent way to rank them for all of the acquired users and subreddits.

## First map-reduce : get the subreddit frequency.

* This map-reduce job is used to calculate the the number of occurrences of each subreddit by counting them all over the number of posts in the dataset.
* The "topness" of a subreddit is computed by summing the number of up-votes with the down-votes it took, as this resembles the amount of interaction each subreddit has.
* I have tried using 1 as the score and it changed the order of subreddits (discussed below)

### Observations

There wasn't anything unique to expect from this map-reduce as it is used to be further processed by the following map-reduce. 

* The range of values varies so much between `0` to almost `500000 ` (i found it by random searching). 

  

## Second map-reduce : Get the top `x` subreddits.

* This map-reduce job is used to get the top subreddits.

### Observations

* The range of values varies so much between `0` to exactly `921524 `.
* The difference in policy changed the order drastically which means that there is a difference between the interactivity of a post and the posting rate in it.
* It's also worth mentioning that you can find the top 10 subreddits in either columns , which means that  number of posts and interaction is correlated after all. However, this doesn't hold for all of them . For example, the `IAmA` page is showing in the up and down votes policy but not in the other one. This subreddit is based on posting personal stories and people reacting over it, unlike `Pokemongiveaway`that appears in the 1 policy but not the other.`Pokemongiveaway` is based on sending gifts and giveaways to the users only, a thing that doesn't require that much of interaction.
* Both of lists shows that top subreddits are concerned with gaming ,then sport and finally movies and entertainment.

| The list of top subreddits using up-vote+down-vote score policy | The list of top subreddits using the score of all subreddits equal to 1 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| AskReddit	921524<br/>pics	206892<br/>funny	180731<br/>videos	179014<br/>todayilearned	159755<br/>soccer	133328<br/>CFB	127766<br/>WTF	120093<br/>AdviceAnimals	119033<br/>worldnews	108723<br/>nfl	104976<br/>leagueoflegends	102615<br/>nba	91818<br/>hiphopheads	76996<br/>gaming	68659<br/>news	62441<br/>hockey	52804<br/>IAmA	50723<br/>gifs	48162<br/>movies	44180<br/>technology	41663<br/>pcmasterrace	40405<br/>TumblrInAction	38274<br/>explainlikeimfive	37639<br/>DotA2	37609<br/>SquaredCircle	36281<br/>nottheonion	34676<br/>relationships	34475<br/>trees	31103<br/>DestinyTheGame	27685<br/>AskMen	27288<br/>smashbros	27150<br/>Games	25844<br/>aww	24780<br/>GlobalOffensive	24683<br/>anime	24524<br/>Showerthoughts	23240<br/>BlackPeopleTwitter	23089<br/>fatpeoplehate	23055<br/>hearthstone	21407<br/>tifu	21157<br/>serialpodcast	21069<br/>atheism	19919<br/>KotakuInAction	19888<br/>Music	19018<br/>mildlyinteresting	17777<br/>cringepics	17762<br/>Jokes	17159<br/>magicTCG	16968<br/>wow	16683 | AskReddit	81813<br/>CFB	22836<br/>funny	18465<br/>pics	18176<br/>pcmasterrace	15148<br/>leagueoflegends	14424<br/>soccer	14115<br/>todayilearned	13419<br/>hockey	11781<br/>worldnews	10993<br/>videos	10619<br/>AdviceAnimals	10302<br/>nba	9998<br/>DotA2	9897<br/>GlobalOffensive	8948<br/>news	8554<br/>WTF	8321<br/>DestinyTheGame	8233<br/>nfl	8059<br/>gaming	7777<br/>movies	6915<br/>CasualConversation	6031<br/>explainlikeimfive	5403<br/>anime	5085<br/>SquaredCircle	4675<br/>pokemontrades	4317<br/>GlobalOffensiveTrade	4070<br/>serialpodcast	4056<br/>smashbros	4019<br/>Random_Acts_Of_Amazon	4000<br/>Games	3831<br/>trees	3817<br/>technology	3725<br/>electronic_cigarette	3715<br/>Pokemongiveaway	3674<br/>TumblrInAction	3585<br/>wow	3531<br/>gifs	3481<br/>politics	3475<br/>gonewild	3474<br/>hiphopheads	3372<br/>Showerthoughts	3352<br/>buildapc	3321<br/>atheism	3259<br/>teenagers	3250<br/>nottheonion	3245<br/>aww	3218<br/>reddevils	3176<br/>PokemonPlaza	3152<br/>relationships	3011 |

## Third map-reduce : get the topics frequency for each subreddit and user.

* This map-reduce job is used to calculate the the number of occurrences of each topic by counting them all over the number of posts in the dataset for top subreddits or users posting on top subreddits.
* To get the topics from body of each post, we need to remove irrelevant words from the file, hence we did the following in eac

### Observations

There wasn't anything unique to expect from this map-reduce as it is used to be further processed by the following map-reduce. 

* The range of values varies so much between `0` to almost `500000 ` (i found it by random searching). 

  