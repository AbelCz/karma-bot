# karma-bot
A highly advanced bot to farm karma on Reddit 

The code in this project is aimed at creating a highly effective comment karma bot on reddit that is both hard to detect and
active on the site. The content it posts is scraped from many different sites, which makes it difficult to track down, and specific waiting 
intervals ensure that no lengthy comments are made too early (which is one of the main reasons people report potential bots). 

Here are a few noteworthy features that make it extremely hard to catch:

- Wait 5 minutes before posting anything

- Remove emojis 

- Randomly substitute common words (i.e. "the President" for "Trump", or "Thanks" with "Thank you")

- Comment frequently in AskReddit with responses from a third party site (Yahoo Answers!)
 
  - This is immediately less suspicious to people who think it just steals comments 
  
  - When doing this, the bot substitutes normal unicode characters for [confusables](http://unicode.org/cldr/utility/confusables.jsp), thwarting those who like to actively search Google for repost bots
  
- Comment in many places across Reddit, so far the following sites are supported: WashingtonPost, Independent.co.uk, YouTube, and Twitter

  - Each of these sites will only be scraped if there are many comments, and the comment selected will be obscure (not on the first page, few replies, unnoticed but somewhat upvoted)

- Auto-delete every comment with a -2 score in case it gets called out and a witchhunt ensues 

I have decided to share this since I no longer have any interest in running karma bots and believe it could be a valuable learning resource. Please use responsibly.

