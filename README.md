# ДЗ №3 К занятию “Разработка смарт-контрактов”
## Выполнил работу Миленин Иван (M33351)

**Задание:** 

- подключиться к Ethereum ноде и замониторить отправку цен токенов: USDT/ETH, USDC/ETH и LINK/ETH из Chainlink
    - зарегистрироваться и получить бесплатный доступ к archive ноде Ethereum в сервисе Alchemy
    - найти oracle feeds для заданных пар токенов в Chainlink
        - пары: ETH/USD, LINK/ETH, USDT/ETH
    - написать монитор:
        - непрерывно мониторящий последние блоки
        - выводящий в лог все новые события изменения цен
        
___________________

Итак, алгоритм выполнения был следующий:
1) Получить доступ к archive ноде Ethereum в сервисе Alchemy - [OK]
2) Найти oracle feeds для заданных пар токенов в Chainlink. 

Найдя пары ETH / USD, LINK / ETH, USDT / ETH в Chainlink я перешел к их `Contract address`, однако 
немного посмотрев их последние транзакции, понял, что они не обновляли несколько лет. После этого я
обратился к нашему чату и обнаружил, что необходимо ипользовать их агрегатора, что я и сделал. 
Таким образом Их агрегаторы имели следующие контаркты:
```
eth_usd  = '0x37bC7498f4FF12C19678ee8fE19d713b87F6a9e6'
link_eth = '0xbba12740DE905707251525477bAD74985DeC46D2'
usdt_eth = '0x7De0d6fce0C128395C488cb4Df667cdbfb35d7DE'
```

3) Написать монитор, непрерывно мониторящий последние блоки и выводящий в лог все новые события изменения цен.

Это было реализовано на питоне засчет библиотеки `Web3`. Код в нем максимально простой, так что думаю, что в 
каких-либо пояснениях не нуждается.

### Вывод в лог
```

C:\Users\SKAT\Desktop\CT-Blockchain-HW3\template>python main.py
2022-11-04 00:26:15.536116| Start connection with eth_usd, Filter for 0xd4cee4c2f5614e56db2edb8ced7a7c99
2022-11-04 00:26:15.698605| Start connection with link_eth, Filter for 0x9b36f78398d3e3e776e99b2e1834111
2022-11-04 00:26:15.870589| Start connection with usdt_eth, Filter for 0x231222bc717c2334f1417141a3985d2e
2022-11-04 00:55:45.147134 :::: |eth_usd| current: 154195000000; roundId: 36215; updatedAt: 1667512535;
2022-11-04 01:17:42.637047 :::: |eth_usd| current: 153073801494; roundId: 36216; updatedAt: 1667513855;
2022-11-04 01:22:43.837084 :::: |usdt_eth| current: 653830910000000; roundId: 8245; updatedAt: 1667514155;
2022-11-04 01:55:42.694945 :::: |eth_usd| current: 153132565354; roundId: 36217; updatedAt: 1667516135;
2022-11-04 02:55:42.875261 :::: |eth_usd| current: 153136402625; roundId: 36218; updatedAt: 1667519735;
2022-11-04 03:23:43.294176 :::: |eth_usd| current: 153904637804; roundId: 36219; updatedAt: 1667521415;
2022-11-04 03:55:42.796403 :::: |eth_usd| current: 153948977591; roundId: 36220; updatedAt: 1667523335;
2022-11-04 04:07:30.677331 :::: |link_eth| current: 5104761500000000; roundId: 5831; updatedAt: 1667524043;
2022-11-04 04:55:30.415224 :::: |eth_usd| current: 153839000000; roundId: 36221; updatedAt: 1667526923;
2022-11-04 05:41:33.453675 :::: |link_eth| current: 5156002873799381; roundId: 5832; updatedAt: 1667529683;
2022-11-04 05:55:43.988924 :::: |eth_usd| current: 154092187044; roundId: 36222; updatedAt: 1667530535;
2022-11-04 05:59:31.186602 :::: |link_eth| current: 5213306235407686; roundId: 5833; updatedAt: 1667530763;
2022-11-04 06:12:34.964753 :::: |link_eth| current: 5277413900000000; roundId: 5834; updatedAt: 1667531543;
2022-11-04 06:24:31.952774 :::: |link_eth| current: 5335126216367203; roundId: 5835; updatedAt: 1667532263;
2022-11-04 06:38:31.450235 :::: |usdt_eth| current: 647226182344694; roundId: 8246; updatedAt: 1667533103;
2022-11-04 06:43:30.933156 :::: |link_eth| current: 5281185000000000; roundId: 5836; updatedAt: 1667533403;
2022-11-04 06:47:07.250768 :::: |eth_usd| current: 154869262073; roundId: 36223; updatedAt: 1667533619;
2022-11-04 06:55:43.249931 :::: |eth_usd| current: 154831029149; roundId: 36224; updatedAt: 1667534135;
2022-11-04 07:09:09.037994 :::: |link_eth| current: 5343806351569833; roundId: 5837; updatedAt: 1667534939;
2022-11-04 07:55:42.686863 :::: |eth_usd| current: 155010901013; roundId: 36225; updatedAt: 1667537735;
2022-11-04 08:25:06.675789 :::: |link_eth| current: 5288721688268186; roundId: 5838; updatedAt: 1667539499;
2022-11-04 08:51:43.841033 :::: |eth_usd| current: 155957000000; roundId: 36226; updatedAt: 1667541095;
2022-11-04 08:55:45.223085 :::: |eth_usd| current: 156421197907; roundId: 36227; updatedAt: 1667541335;
2022-11-04 08:55:45.406277 :::: |link_eth| current: 5234975753931189; roundId: 5839; updatedAt: 1667541335;
2022-11-04 08:56:43.719823 :::: |usdt_eth| current: 639869980000000; roundId: 8247; updatedAt: 1667541395;
2022-11-04 09:21:19.270864 :::: |eth_usd| current: 157274957409; roundId: 36228; updatedAt: 1667542871;
2022-11-04 09:33:20.550280 :::: |eth_usd| current: 158123000000; roundId: 36229; updatedAt: 1667543591;
2022-11-04 09:34:19.099738 :::: |usdt_eth| current: 633198230000000; roundId: 8248; updatedAt: 1667543651;
2022-11-04 09:55:43.673171 :::: |eth_usd| current: 158090000000; roundId: 36230; updatedAt: 1667544935;
```

Для запуска необходимо выполнить следующее:
```
python template\main.py
```