import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


def get_count(dut):
    return int(dut.uo_out.value) & 0xF


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start 4-bit Counter Test")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset counter
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 3)
    assert get_count(dut) == 0

    # Release reset, enable low
    dut.rst_n.value = 1
    dut.ui_in[0].value = 0
    await ClockCycles(dut.clk, 3)
    assert get_count(dut) == 0

    # Enable counter
    dut.ui_in[0].value = 1
    await ClockCycles(dut.clk, 1)
    assert get_count(dut) == 1

    await ClockCycles(dut.clk, 1)
    assert get_count(dut) == 2

    await ClockCycles(dut.clk, 1)
    assert get_count(dut) == 3

    # Disable and hold value
    dut.ui_in[0].value = 0
    hold_value = get_count(dut)
    await ClockCycles(dut.clk, 3)
    assert get_count(dut) == hold_value

    # Enable again
    dut.ui_in[0].value = 1
    await ClockCycles(dut.clk, 2)
    assert get_count(dut) == ((hold_value + 2) & 0xF)

    # Reset again
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    assert get_count(dut) == 0

    dut._log.info("4-bit Counter Test Completed")
