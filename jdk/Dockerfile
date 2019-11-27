#
#

FROM openjdk

# RUN apt-get update && apt-get install -y maven
# fix maven installation based on
# [How do I install Maven with Yum?](https://stackoverflow.com/questions/7532928/how-do-i-install-maven-with-yum)
RUN yum -y install wget
RUN wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
RUN yum -y install apache-maven

EXPOSE 8080

# ADD ./idle.sh /

# CMD sh /idle.sh