<?php
declare(strict_types=1);

namespace Strategy\Php\Strategies;

use InvalidArgumentException;
use Strategy\Php\Order;
use Strategy\Php\ShippingQuote;
use Strategy\Php\ShippingStrategy;

final class FlatRateStrategy implements ShippingStrategy
{
    public function name(): string { return 'flat_rate'; }

    public function supports(Order $order): bool
    {
        return $order->destination === 'local' && $order->totalWeightKg <= 10;
    }

    public function validate(Order $order): void
    {
        if ($order->totalWeightKg < 0) {
            throw new InvalidArgumentException('Weight cannot be negative.');
        }
    }

    public function quote(Order $order): ShippingQuote
    {
        $base = 99; 
        $eta  = 2;
        if ($order->express) {
            $base += 60;
            $eta = max(1, $eta - 1);
        }

        return new ShippingQuote(
            cost: round($base, 2),
            etaDays: $eta,
            breakdown: [
                'strategy' => $this->name(),
                'base' => $base,
                'express' => $order->express,
            ]
        );
    }
}