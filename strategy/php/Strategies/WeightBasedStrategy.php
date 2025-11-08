<?php
declare(strict_types=1);

namespace Strategy\Php\Strategies;
use InvalidArgumentException;
use Strategy\Php\Order;
use Strategy\Php\ShippingQuote;
use Strategy\Php\ShippingStrategy;

final class WeightBasedStrategy implements ShippingStrategy
{
    public function name(): string { return 'weight_based'; }

    public function supports(Order $order): bool
    {
        return in_array($order->destination, ['local', 'z1', 'z2'], true)
            && $order->totalWeightKg <= 30;
    }

    public function validate(Order $order): void
    {
        if ($order->totalWeightKg <= 0) {
            throw new InvalidArgumentException('Weight must be > 0 for weight-based shipping.');
        }
    }

    public function quote(Order $order): ShippingQuote
    {
        $perKg = match ($order->destination) {
            'local' => 25,
            'z1'    => 40,
            'z2'    => 55,
            default => 70
        };

        $cost = 60 + ($order->totalWeightKg * $perKg);
        $eta  = match ($order->destination) {
            'local' => 2,
            'z1'    => 3,
            'z2'    => 4,
            default => 5
        };

        if ($order->express) {
            $cost *= 1.25;
            $eta = max(1, $eta - 1);
        }

        return new ShippingQuote(
            cost: round($cost, 2),
            etaDays: $eta,
            breakdown: [
                'strategy'      => $this->name(),
                'base'          => 60,
                'perKg'         => $perKg,
                'weightKg'      => $order->totalWeightKg,
                'expressBoost'  => $order->express ? 'x1.25' : 'x1.00',
            ]
        );
    }
}