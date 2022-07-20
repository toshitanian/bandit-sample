
Contents delivery server selects contents using Multi-arm bandit algorithm.

refers to: https://zenn.dev/5nta/articles/78361b28d414b54df29b

```bash
$ poetry run python contents_server.py
```

```bash
====0:user-dog====
clicks     :	{'dog': 1, 'cat': 0, 'bird': 0}
server imps:	{'dog': 1, 'cat': 0, 'bird': 0}
CTRs       :	{'dog': 1.0, 'cat': 0, 'bird': 0}
total CTR  :	1.0
====10000:user-dog====
clicks     :	{'dog': 7029, 'cat': 5, 'bird': 2}
server imps:	{'dog': 9973, 'cat': 17, 'bird': 11}
CTRs       :	{'dog': 0.7048029680136368, 'cat': 0.29411764705882354, 'bird': 0.18181818181818182}
total CTR  :	0.7035296470352965
====20000:user-dog====
clicks     :	{'dog': 13973, 'cat': 5, 'bird': 4}
server imps:	{'dog': 19967, 'cat': 18, 'bird': 16}
CTRs       :	{'dog': 0.6998046777182351, 'cat': 0.2777777777777778, 'bird': 0.25}
total CTR  :	0.6990650467476626
====30000:user-dog====
clicks     :	{'dog': 20964, 'cat': 5, 'bird': 4}
server imps:	{'dog': 29967, 'cat': 18, 'bird': 16}
CTRs       :	{'dog': 0.6995695264791271, 'cat': 0.2777777777777778, 'bird': 0.25}
total CTR  :	0.6990766974434186
====40000:user-dog====
clicks     :	{'dog': 28029, 'cat': 5, 'bird': 4}
server imps:	{'dog': 39964, 'cat': 19, 'bird': 18}
CTRs       :	{'dog': 0.7013562205985386, 'cat': 0.2631578947368421, 'bird': 0.2222222222222222}
total CTR  :	0.7009324766880828
====50000:user-dog====
clicks     :	{'dog': 34992, 'cat': 6, 'bird': 4}
server imps:	{'dog': 49963, 'cat': 20, 'bird': 18}
CTRs       :	{'dog': 0.7003582651161859, 'cat': 0.3, 'bird': 0.2222222222222222}
total CTR  :	0.7000259994800104
====60000:user-dog====
clicks     :	{'dog': 41929, 'cat': 6, 'bird': 4}
server imps:	{'dog': 59963, 'cat': 20, 'bird': 18}
CTRs       :	{'dog': 0.6992478695195371, 'cat': 0.3, 'bird': 0.2222222222222222}
total CTR  :	0.6989716838052699
====70000:user-dog====
clicks     :	{'dog': 48962, 'cat': 6, 'bird': 4}
server imps:	{'dog': 69962, 'cat': 21, 'bird': 18}
CTRs       :	{'dog': 0.6998370544009606, 'cat': 0.2857142857142857, 'bird': 0.2222222222222222}
total CTR  :	0.6995900058570592
```