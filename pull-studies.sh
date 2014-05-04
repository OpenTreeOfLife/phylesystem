#!/bin/bash
pushd . >/dev/null
scriptdir=$(dirname "$0")
cd $scriptdir
for giturl in $(cat shard-list.txt)
do
    shardreponame=$(echo $giturl | sed -E 's/.*\///' | sed -E 's/\.git//')
    rd=$(echo "shards/$shardreponame")
    if test -d "$rd"
    then
        cd "$rd"
        echo "pulling to update $shardreponame"
        git pull origin master
    else
        cd shards
        echo "cloning $giturl"
        git clone "$giturl"
    fi
    cd - > /dev/null
done

popd >/dev/null
