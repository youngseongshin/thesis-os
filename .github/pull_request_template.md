## Summary

## Agent ownership

- [ ] Alpha
- [ ] Lattice
- [ ] Arki

## Public/private boundary checked

- [ ] No secrets
- [ ] No private portfolio data
- [ ] No cookies or OAuth sessions
- [ ] No paid raw data

## Tests

```bash
python -m thesis_os lint --root .
python -m thesis_os demo --out /tmp/thesis-os-demo
python -m unittest discover -s tests
```
