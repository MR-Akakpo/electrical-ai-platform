from app.engineering.short_circuit.short_circuit_engine import (
    run_short_circuit_analysis
)


def calculate_short_circuit_capacity(
    transformer_power_kva: float,
    voltage_v: float,
    impedance_percent: float,
    xr_ratio: float = 10,
    breaker_capacity_ka: float = 36,
    fault_duration_s: float = 1
):

    result = run_short_circuit_analysis(
        transformer_power_kva=transformer_power_kva,
        voltage_v=voltage_v,
        impedance_percent=impedance_percent,
        xr_ratio=xr_ratio,
        breaker_capacity_ka=breaker_capacity_ka,
        fault_duration_s=fault_duration_s
    )

    return result


# backward compatibility
run_short_circuit_study = calculate_short_circuit_capacity
