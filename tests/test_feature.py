from pages.feature_page import FeaturePage

def test_p2_youtube_search_tech_news(page):
    feature = FeaturePage(page)
    feature.open('https://www.youtube.com')
    feature.search('latest tech news')
    feature.submit_search()
    feature.wait_for_results()
    feature.screenshot('result.png')