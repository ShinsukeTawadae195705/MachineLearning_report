from icrawler.builtin import BingImageCrawler

#各ヒロイン達の名前での検索 & タイトルによるランダム検索
keywords = ["五等分の花嫁　一花", "五等分の花嫁　二乃","五等分の花嫁　三玖","五等分の花嫁　四葉","五等分の花嫁　五月","五等分の花嫁"]
filenames = ["Ichika", "Nino", "Miku", "Yotsuba","Itsuki","All"]

for i in range(len(keywords)):
    crawler = BingImageCrawler(storage={"root_dir": filenames[i]})
    crawler.crawl(keyword=keywords[i], max_num=1000)