package main

import (
	payments_factory "design.pattern.com/go/factory"
	payments "design.pattern.com/go/problem"
	payments_interface "design.pattern.com/go/solution"
)

func main() {
	approach1()
	approach2()
	approach3()
}

func approach1() {

	choice := "paypal"

	switch choice {
	case "paypal":
		paypal := payments.PayPal{}
		checkoutPayPal(paypal, 1000)
	case "stripe":
		stripe := payments.Stripe{}
		checkoutStripe(stripe, 1000)
	case "apple":
		applePay := payments.ApplePay{}
		checkoutApplePay(applePay, 1000)
	}
}

// Checkout for Paypal
func checkoutPayPal(payment payments.PayPal, amount float64) {
	payment.Pay(amount)
}

// Checkout for Stripe
func checkoutStripe(payment payments.Stripe, amount float64) {
	payment.Pay(amount)
}

// Checkout for ApplePay
func checkoutApplePay(payment payments.ApplePay, amount float64) {
	payment.Pay(amount)
}

func approach2() {

	choice := "paypal"
	switch choice {
	case "paypal":
		paypal := payments.PayPal{} // Paypal type
		checkout(paypal, 1000)
	case "stripe":
		stripe := payments.Stripe{} // Stripe type
		checkout(stripe, 1000)
	case "apple":
		apple_pay := payments.ApplePay{} // ApplePay type
		checkout(apple_pay, 1000)

	}

}

func approach3() {
	choice := "paypal"
	payment, _ := payments_factory.PaymentFactory(choice)
	checkout(payment, 1000)
}

// One function handling payment, notice it takes PaymentGateway type
// because our payment types implement this interface, so their objects can be passed here
func checkout(payment payments_interface.PaymentGateway, amount float64) {
	payment.Pay(amount)
}
