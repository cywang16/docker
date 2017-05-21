#
# build: sudo docker build -t tomcatkeycloak .
# execution: sudo docker run -d -p 880:8080 -v $(pwd)/Shares:/mnt/shares -it tomcatkeycloak
#
FROM tomcat
MAINTAINER Chun-Yen Wang

RUN wget -qO- https://downloads.jboss.org/keycloak/3.0.0.Final/adapters/keycloak-oidc/keycloak-tomcat8-adapter-dist-3.0.0.Final.tar.gz | tar xvz -C /usr/local/tomcat/lib
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml

EXPOSE 8080