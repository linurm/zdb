static main(void)
{
  auto bpt;

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x6140);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xb700);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xb754);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xb788);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xb7b0);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xb9f4);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xb9f8);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbbf0);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbd68);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbe10);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbe14);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbf2c);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbf30);
  Breakpoints.Add(bpt);
}
