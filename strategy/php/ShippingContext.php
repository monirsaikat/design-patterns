<?php

namespace Strategy\Php;

use RuntimeException;

final class ShippingContext
{
    public function __construct(private ShippingStrategy $strategy) {}

    public function setStrategy(ShippingStrategy $strategy): void
    {
        $this->strategy = $strategy;
    }

    public function getStrategyName(): string
    {
        return $this->strategy->name();
    }

    public function quote(Order $order): ShippingQuote
    {
        if (!$this->strategy->supports($order)) {
            throw new RuntimeException("Strategy '{$this->strategy->name()}' does not support this order.");
        }
        $this->strategy->validate($order);
        return $this->strategy->quote($order);
    }
}