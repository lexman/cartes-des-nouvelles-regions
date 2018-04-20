if [ ! -d env ] ; then
    virtualenv env
fi

. env/bin/activate

if [ ! -d ./env/lib/python2.7/site-packages/tuttle ] ; then
    pip install https://github.com/lexman/tuttle/archive/v0.6-dev2.zip
fi

tuttle invalidate
tuttle run -j 8
