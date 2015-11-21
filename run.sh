#!/bin/bash
echo "run the spider"

base_dir=~/ncuscrapy

git fetch
git pull

if [ ! -f "$base_dir/env/bin/activate" ]
then
	# cd $project_env
	virtualenv {$base_dir}/env
	
fi


source  $base_dir/env/bin/activate
{$base_dir}/env/bin/pip install -r {$base_dir}/ncu/requirements.txt
cd {$base_dir}/ncu/ncu
scrapy crawl activity
scrapy crawl affiche
scrapy crawl eduaffiche
scrapy crawl news
python {$base_dir}/ncu/ncu/send.py
