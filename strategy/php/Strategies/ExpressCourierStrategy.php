<?php
declare(strict_types=1);

namespace Strategy\Php\Strategies;
use InvalidArgumentException;
use Strategy\Php\Order;
use Strategy\Php\ShippingQuote;
use Strategy\Php\ShippingStrategy;

final class ExpressCourierStrategy implements ShippingStrategy
{
    public function name(): string { return 'express_courier'; }

    public function supports(Order $order): bool
    {
        return $order->express && $order->totalWeightKg <= 15;
    }

    public function validate(Order $order): void
    {
        if ($order->totalWeightKg > 15) {
            throw new InvalidArgumentException('Express courier supports up to 15kg.');
        }
    }

    public function quote(Order $order): ShippingQuote
    {
        $zoneFactor = match ($order->destination) {
            'local' => 1.0, 'z1' => 1.2, 'z2' => 1.4, 'intl' => 2.5, default => 1.6
        };

        $cost = 150 + ($order->totalWeightKg * 90) * $zoneFactor;
        $eta  = ($order->destination === 'local') ? 1 : 2;

        return new ShippingQuote(
            cost: round($cost, 2),
            etaDays: $eta,
            breakdown: [
                'strategy'   => $this->name(),
                'zoneFactor' => $zoneFactor,
                'weightKg'   => $order->totalWeightKg,
            ]
        );
    }
}
