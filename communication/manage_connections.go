package main

import (
	"log"
	"net"
)

func manageConnections() {
	// إنشاء خادم للاستماع إلى الاتصالات
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatalf("حدث خطأ أثناء إعداد الخادم: %s", err)
	}
	defer listener.Close()
	log.Println("الخادم جاهز ويستمع على المنفذ 8080")

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Printf("حدث خطأ أثناء قبول الاتصال: %s", err)
			continue
		}
		log.Println("تم قبول اتصال جديد")
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	// معالجة الاتصال
	defer conn.Close()
	log.Println("تم معالجة الاتصال")
}

func main() {
	manageConnections()
}
