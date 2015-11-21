#!/bin/bash
echo "run the spider"

base_dir=~/ncuscrapy

git pull

if [ ! -f "$base_dir/env/bin/activate" ]
then
	# cd $project_env
	virtualenv {$base_dir}/env
	
fi

cd ~
source  $base_dir/env/bin/activate
$base_dir/env/bin/pip install -r ncuscrapy/ncu/requirements.txt
scrapy crawl activity
scrapy crawl affiche
scrapy crawl eduaffiche
scrapy crawl news
python {$base_dir}/ncuscrapy/ncu/ncu/send
