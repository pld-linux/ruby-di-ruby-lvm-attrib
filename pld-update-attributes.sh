#!/bin/sh
# Creates branch for GitHub PR to submit upstream new LVM version attributes
# Version is taken as version of device-mapper-devel package
#
# Usage:
# ./pld-update-attributes.sh
# Author: Elan Ruusamäe <glen@pld-linux.org>
#

git_url=git@github.com:gregsymons/di-ruby-lvm-attrib.git
dir=di-ruby-lvm-attrib
set -e

if [ ! -d "$dir" ]; then
	git clone $git_url $dir --depth=1
fi

cd $dir

git checkout next
git pull --rebase
lvm_version=$(rpm -q device-mapper-devel --qf '%{V}')
tag_ver=v$(echo "$lvm_version" | tr . _)

./update-lvm.sh "$tag_ver"

git_branch=$(git rev-parse --abbrev-ref HEAD)

dir=$(pwd)

cat <<EOF
To push, run in $dir:

  git push --set-upstream origin $git_branch

EOF
