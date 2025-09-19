package solution

import "fmt"

type PaymentGateway interface {
	Pay(amount float64) // Common behaviour for all payment types
}

type PayPal struct{}
type Stripe struct{}

func (p PayPal) Pay(amount float64) {
	fmt.Println("Paid with PayPal:", amount)
}

func (s Stripe) Pay(amount float64) {
	fmt.Println("Paid with Stripe:", amount)
}

type ApplePay struct{}

func (s ApplePay) Pay(amount float64) {
	fmt.Println("Paid with Apple:", amount)
}
