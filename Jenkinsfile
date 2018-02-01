/**
  Workfow to download and execute a SSL Test connexion
  @author kuisatahverat
 **/
env.targetHost = targetHost
node () {
  stage ('Env'){
    sh 'export'
  }
  stage ('Download sources'){
    tool name: 'Default', type: 'hudson.plugins.git.GitTool'
    git 'github.com/kuisathaverat/TestSSLServer.git'
  }
  stage ('Compile sources'){
    //tool name: 'maven3', type: 'hudson.tasks.Maven$MavenInstallation'
    sh 'mvn clean compile'
  }
 stage ('Execute Test SSL handshake for microsites.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=microsites.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for images.j2.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=images.j2.comexec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.efax.com.au'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.efax.com.au
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for scansnap.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=scansnap.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www.j2.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www.j2.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for ads.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=ads.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www.metrofax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www.metrofax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for m.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=m.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.efax.de'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.efax.de
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.efax.co.jp'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.efax.co.jp
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.efax.co.uk'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.efax.co.uk
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.efax.es'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.efax.es
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www.efaxcorporate.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www.efaxcorporate.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.it.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.it.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for en2.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=en2.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.efax.fr'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.efax.fr
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for myaccount.metrofax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=myaccount.metrofax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.mbox.com.au'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.mbox.com.au
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www.j2corporate.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www.j2corporate.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.be.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.be.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www.efax.pl'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www.efax.pl
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for api.fax.j2.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=api.fax.j2.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for api.mobile.j2.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=api.mobile.j2.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www.ereceptionist.co.uk'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www.ereceptionist.co.uk
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.efax.com.au'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.efax.com.au
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.efax.nl'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.efax.nl
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for ads.evoice.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=ads.evoice.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for my.metrofax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=my.metrofax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www.efax.pt'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www.efax.pt
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for m.onebox.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=m.onebox.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.efax.fr'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.efax.fr
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for ads.j2.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=ads.j2.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for m.metrofax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=m.metrofax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.efax.co.jp'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.efax.co.jp
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.efax.nl'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.efax.nl
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.mbox.com.au'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.mbox.com.au
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for jconnect.j2.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=jconnect.j2.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www.ereceptionist.nl'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www.ereceptionist.nl
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.it.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.it.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www2.efax.de'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www2.efax.de
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for it.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=it.efax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.efax.es'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.efax.es
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for central.myfax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=central.myfax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for portal.jfax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=portal.jfax.com
  exec:java'
 }


 }
 stage ('Execute Test SSL handshake for www.efax.com'){
   sh 'mvn -Djavax.net.debug=ssl:handshake -Dexec.mainClass=org.bolet.TestSSLHandShake -Dexec.args=www.efax.com
  exec:java'
 }

}
}
