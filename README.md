Yelp Analysis Tools
by Jesse Singh
www.jessesingh.com/blog/yelpreviews.html
Saturday, September 29, 2012

A set of analysis and visualization functions written in Python specifically for the Yelp Academic Dataset (download here: http://www.yelp.com/academic_dataset). It can be easily branched for any other dataset and should be particularly self-explanatory.

Example Usage:
import yelp_analysis_tools as yat
reviews, businesses, users = yat.importJSON(dataset)
prolificUsers = [u['user_id'] for u in users if u['review_count'] > 500]
prolificUsersReviewDates = [r['date'] for r in reviews if r['user_id'] in prolificUsers]
prolificUsersReviewDays = yat.convertDatesToDays(prolificUsersReviewDates)
prolificDays = yat.get_counts(prolificUsersReviewDays)
yat.buildBarDayPlot(prolificDays, title="Days Prolific Users Reviewed Businesses")