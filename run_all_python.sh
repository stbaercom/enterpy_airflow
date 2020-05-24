

rm data/*.{csv,db,pptx}
rm data/ftp/*.{txt,pptx}


python a00_get_prices.py
sleep 5

python a00_get_prices.py
sleep 5


python a00_get_prices.py
sleep 5


python a01_calc_stats.py

python a02_do_report.py