#/bin/bsah
#author nuanxiansheng
#date 201804013
#just for a github test
#DATE/TIME
CDATE=$(date "+%Y-%m-%d")
CTIME=$(date "+%Y-%m-%d-%H-%M")

#shell
www_dir="/var/www/html"
code_dir="/data/servers/deploy/code/demo"
tar_dir="/data/servers/deploy/tar"
config_dir="/data/servers/deploy/config"
tmp_dir="/data/servers/deploy/tmp"

usage() {
		echo $"Usage: $0 [deploy | rollback-list | rollback-pro ver]"
}

git_pull_pro() {
	echo "git pull begin............."
	cd "$code_dir" && git pull
	api_verl=$(git show | grep commit | cut -d ' ' -f2)
	api_ver=$(echo ${api_verl:0:6})
	/bin/cp -r "$code_dir" "$tmp_dir"

}

config_pro() {  
	echo "cp config begin............."
	cp "$config_dir"/* "$tmp_dir"/demo/
	tar_ver="$api_ver"-"$CTIME"
	cd $tmp_dir && mv demo pro_demo_"$tar_ver"	
}

tar_pro() {
	echo "tar  begin.........."
	cd $tmp_dir && tar -czf pro_demo_"$tar_ver".tar.gz pro_demo_"$tar_ver"
	echo "pro_demo_"$tar_ver".tar.gz    tar  end ..............."			
}

scp_pro() {
		echo "scp begin............."
		/bin/cp $tmp_dir/pro_demo_"$tar_ver".tar.gz /tmp

}

deploy_pro() {
	echo "deploy_pro begin............."
	cd /tmp && tar -zxf pro_demo_"$tar_ver".tar.gz
	rm -f $www_dir/demo
	ln -s /tmp/pro_demo_"$tar_ver" $www_dir/demo

}

test_pro() {
	echo "test begin...................."
	echo "test Ok ......................"
}

rollback_list() {
	ls -l /tmp/*.tar.gz
}

rollback_pro() {
	if [ ! -d "/tmp/$1" ];then
		echo "rollback$1  ------------failed !"
		echo "$1 not exits,you can rollback_list to make sure"
	else
		rm -f $www_dir/demo
		ln -s /tmp/$1 $www_dir/demo
		echo "rollback$1  ----------------Ok"
	fi
}

main() {
case $1 in 
	deploy)
		git_pull_pro;
		config_pro;
		tar_pro;
		scp_pro;
		deploy_pro;
		test_pro;
		;;
	rollback-list)
		rollback_list;	
		;;
	rollback-pro)
		rollback_pro $2;
		;;
	*)
	usage;
esac
}
main $1 $2
