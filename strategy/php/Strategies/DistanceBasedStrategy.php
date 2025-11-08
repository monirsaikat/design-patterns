<?php
declare(strict_types=1);

namespace Strategy\Php\Strategies;

use InvalidArgumentException;
use Strategy\Php\Order;
use Strategy\Php\ShippingQuote;
use Strategy\Php\ShippingStrategy;

final class DistanceBasedStrategy implements ShippingStrategy
{
    public function name(): string { return 'distance_based'; }

    public function supports(Order $order): bool
    {
        return $order->distanceKm > 0 && $order->distanceKm <= 2000;
    }

    public function validate(Order $order): void
    {
        if ($order->distanceKm <= 0) {
            throw new InvalidArgumentException('Distance must be > 0.');
        }
    }

    public function quote(Order $order): ShippingQuote
    {
        $perKm = 0.9; // BDT per km
        $cost  = 80 + ($order->distanceKm * $perKm);
        $eta   = (int)ceil($order->distanceKm / 400); // ~400km/day

        if ($order->express) {
            $cost *= 1.15;
            $eta = max(1, $eta - 1);
        }

        return new ShippingQuote(
            cost: round($cost, 2),
            etaDays: $eta,
            breakdown: [
                'strategy'   => $this->name(),
                'base'       => 80,
                'perKm'      => $perKm,
                'distanceKm' => $order->distanceKm,
            ]
        );
    }
}