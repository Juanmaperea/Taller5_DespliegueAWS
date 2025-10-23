#!/bin/bash
# Usage: ./deploy-ec2.sh <EC2_IP>
EC2_IP=$1
echo "Deploying to $EC2_IP ..."
ssh -i key.pem ec2-user@$EC2_IP <<'EOF'
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo systemctl enable --now docker
sudo usermod -aG docker ec2-user
docker run -d --name pg -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=studentsdb -p 5432:5432 postgres:15
docker pull myuser/student-api:latest
docker stop student-api || true && docker rm student-api || true
docker run -d --name student-api -e DATABASE_URL="postgresql://postgres:postgres@localhost:5432/studentsdb" -p 8000:8000 myuser/student-api:latest
EOF
