echo "starting deployment"

cd /home/ec2-user/eb/mechakaijuwars
git pull origin master
cd /home/ec2-user/eb/mechakaijuwars/platform/app
git add .
git commit -m "automated deployment by elastic beanstalk"
git aws.push

echo "ending deployment"