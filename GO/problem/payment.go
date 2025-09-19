package problem

import "fmt"

type PayPal struct{}
type Stripe struct{}

type ApplePay struct{}

func (p PayPal) Pay(amount float64) {
	fmt.Println("Paid with PayPal:", amount)
}

func (s Stripe) Pay(amount float64) {
	fmt.Println("Paid with Stripe:", amount)
}

func (s ApplePay) Pay(amount float64) {
	fmt.Println("Paid with Apple:", amount)
}
