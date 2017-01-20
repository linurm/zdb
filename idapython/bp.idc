static main(void)
{
  auto bpt;

  bpt = Breakpoint();
  bpt.set_abs_bpt(0x7801121c);
  bpt.type=4;
  bpt.flags=1;
  Breakpoints.Add(bpt);
}
