#
# build: sudo docker build -t tomcatkeycloak .
# execution: sudo docker run -d -p 880:8080 -v $(pwd)/Shares:/mnt/shares -it tomcatkeycloak
#
FROM tomcat
MAINTAINER Chun-Yen Wang

RUN wget -qO- https://downloads.jboss.org/keycloak/2.5.0.CR1/adapters/keycloak-oidc/keycloak-tomcat8-adapter-dist-2.5.0.CR1.tar.gz | tar xvz -C /usr/local/tomcat/lib

EXPOSE 8080