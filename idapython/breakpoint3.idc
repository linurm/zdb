static main(void)
{
  auto bpt;

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x6140);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xb4d8);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xb700);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xb788);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbf2c);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbf30);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbf44);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xbf78);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xc1f4);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xc8a8);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xc8b0);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xc9ac);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xc9b4);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xcac4);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0xe2c0);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x1068c);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x108b0);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x1121c);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x11f14);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x11f80);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x17bbc);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x17c14);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x17e3c);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x17eac);
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x18144);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x18148);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x18568);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x19de0);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x19dfc);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x1b79c);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x1c110);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x1c12c);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x1c29c);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x1cde8);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x1ce68);
  Breakpoints.Add(bpt);
}
