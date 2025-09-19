package factory

import (
	"fmt"

	payments "design.pattern.com/go/solution"
)


func PaymentFactory(method string) (payments.PaymentGateway, error) {
	switch method {
	case "paypal":
		return payments.PayPal{}, nil
	case "stripe":
		return payments.Stripe{}, nil
	// Add new payments here 
	case "apple_pay":
		return payments.ApplePay{}, nil	
	default:
		return nil, fmt.Errorf("unknown payment method: %s", method)
	}
}
