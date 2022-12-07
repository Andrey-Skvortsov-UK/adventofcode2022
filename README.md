# adventofcode2022
Solutions for https://adventofcode.com/


<details close>
<summary>Day 1: Calorie Counting</summary>

<article class="day-desc"><h2> Part 1 </h2><p>Santa's reindeer typically eat regular reindeer food, but they need a lot of <a href="/2018/day/25">magical energy</a> to deliver presents on Christmas. For that, their favorite snack is a special type of <em class="star">star</em> fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.</p>
<p>To supply enough magical energy, the expedition needs to retrieve a minimum of <em class="star">fifty stars</em> by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.</p>
<p>Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants <em class="star">one star</em>. Good luck!</p>
<p>The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of <em>Calories</em> each Elf is carrying (your puzzle input).</p>
<p>The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, <span title="By &quot;etc&quot;, you're pretty sure they just mean &quot;more snacks&quot;.">etc.</span> that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.</p>
<p>For example, suppose the Elves finish writing their items' Calories and end up with the following list:</p>
<pre><code>1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
</code></pre>
<p>This list represents the Calories of the food carried by five Elves:</p>
<ul>
<li>The first Elf is carrying food with <code>1000</code>, <code>2000</code>, and <code>3000</code> Calories, a total of <code><em>6000</em></code> Calories.</li>
<li>The second Elf is carrying one food item with <code><em>4000</em></code> Calories.</li>
<li>The third Elf is carrying food with <code>5000</code> and <code>6000</code> Calories, a total of <code><em>11000</em></code> Calories.</li>
<li>The fourth Elf is carrying food with <code>7000</code>, <code>8000</code>, and <code>9000</code> Calories, a total of <code><em>24000</em></code> Calories.</li>
<li>The fifth Elf is carrying one food item with <code><em>10000</em></code> Calories.</li>
</ul>
<p>In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the <em>most</em> Calories. In the example above, this is <em><code>24000</code></em> (carried by the fourth Elf).</p>
<p>Find the Elf carrying the most Calories. <em>How many total Calories is that Elf carrying?</em></p>
</article>

<article class="day-desc"><h2 id="part2">Part 2</h2>
<p>By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually <em>run out of snacks</em>.</p>
<p>To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the <em>top three</em> Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.</p>
<p>In the example above, the top three Elves are the fourth Elf (with <code>24000</code> Calories), then the third Elf (with <code>11000</code> Calories), then the fifth Elf (with <code>10000</code> Calories). The sum of the Calories carried by these three elves is <code><em>45000</em></code>.</p>
<p>Find the top three Elves carrying the most Calories. <em>How many Calories are those Elves carrying in total?</em></p>
</article>

</details>

<details close>
<summary>Day 2: Rock Paper Scissors</summary>
<article class="day-desc"><h2>Part 1</h2><p>The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant <a href="https://en.wikipedia.org/wiki/Rock_paper_scissors" target="_blank">Rock Paper Scissors</a> tournament is already in progress.</p>
<p>Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.</p>
<p>Appreciative of your help yesterday, one Elf gives you an <em>encrypted strategy guide</em> (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: <code>A</code> for Rock, <code>B</code> for Paper, and <code>C</code> for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.</p>
<p>The second column, <span title="Why do you keep guessing?!">you reason</span>, must be what you should play in response: <code>X</code> for Rock, <code>Y</code> for Paper, and <code>Z</code> for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.</p>
<p>The winner of the whole tournament is the player with the highest score. Your <em>total score</em> is the sum of your scores for each round. The score for a single round is the score for the <em>shape you selected</em> (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the <em>outcome of the round</em> (0 if you lost, 3 if the round was a draw, and 6 if you won).</p>
<p>Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.</p>
<p>For example, suppose you were given the following strategy guide:</p>
<pre><code>A Y
B X
C Z
</code></pre>
<p>This strategy guide predicts and recommends the following:</p>
<ul>
<li>In the first round, your opponent will choose Rock (<code>A</code>), and you should choose Paper (<code>Y</code>). This ends in a win for you with a score of <em>8</em> (2 because you chose Paper + 6 because you won).</li>
<li>In the second round, your opponent will choose Paper (<code>B</code>), and you should choose Rock (<code>X</code>). This ends in a loss for you with a score of <em>1</em> (1 + 0).</li>
<li>The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = <em>6</em>.</li>
</ul>
<p>In this example, if you were to follow the strategy guide, you would get a total score of <code><em>15</em></code> (8 + 1 + 6).</p>
<p><em>What would your total score be if everything goes exactly according to your strategy guide?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: <code>X</code> means you need to lose, <code>Y</code> means you need to end the round in a draw, and <code>Z</code> means you need to win. Good luck!"</p>
<p>The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:</p>
<ul>
<li>In the first round, your opponent will choose Rock (<code>A</code>), and you need the round to end in a draw (<code>Y</code>), so you also choose Rock. This gives you a score of 1 + 3 = <em>4</em>.</li>
<li>In the second round, your opponent will choose Paper (<code>B</code>), and you choose Rock so you lose (<code>X</code>) with a score of 1 + 0 = <em>1</em>.</li>
<li>In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = <em>7</em>.</li>
</ul>
<p>Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of <code><em>12</em></code>.</p>
<p>Following the Elf's instructions for the second column, <em>what would your total score be if everything goes exactly according to your strategy guide?</em></p>
</article>
</details>

<details close>
<summary>Day 3: Rucksack Reorganization</summary>
<article class="day-desc"><h2>Part 1</h2><p>One Elf has the important job of loading all of the <a href="https://en.wikipedia.org/wiki/Rucksack" target="_blank">rucksacks</a> with supplies for the <span title="Where there's jungle, there's hijinxs.">jungle</span> journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.</p>
<p>Each rucksack has two large <em>compartments</em>. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.</p>
<p>The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, <code>a</code> and <code>A</code> refer to different types of items).</p>
<p>The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.</p>
<p>For example, suppose you have the following list of contents from six rucksacks:</p>
<pre><code>vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
</code></pre>
<ul>
<li>The first rucksack contains the items <code>vJrwpWtwJgWrhcsFMMfFFhFp</code>, which means its first compartment contains the items <code>vJrwpWtwJgWr</code>, while the second compartment contains the items <code>hcsFMMfFFhFp</code>. The only item type that appears in both compartments is lowercase <code><em>p</em></code>.</li>
<li>The second rucksack's compartments contain <code>jqHRNqRjqzjGDLGL</code> and <code>rsFMfFZSrLrFZsSL</code>. The only item type that appears in both compartments is uppercase <code><em>L</em></code>.</li>
<li>The third rucksack's compartments contain <code>PmmdzqPrV</code> and <code>vPwwTWBwg</code>; the only common item type is uppercase <code><em>P</em></code>.</li>
<li>The fourth rucksack's compartments only share item type <code><em>v</em></code>.</li>
<li>The fifth rucksack's compartments only share item type <code><em>t</em></code>.</li>
<li>The sixth rucksack's compartments only share item type <code><em>s</em></code>.</li>
</ul>
<p>To help prioritize item rearrangement, every item type can be converted to a <em>priority</em>:</p>
<ul>
<li>Lowercase item types <code>a</code> through <code>z</code> have priorities 1 through 26.</li>
<li>Uppercase item types <code>A</code> through <code>Z</code> have priorities 27 through 52.</li>
</ul>
<p>In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (<code>p</code>), 38 (<code>L</code>), 42 (<code>P</code>), 22 (<code>v</code>), 20 (<code>t</code>), and 19 (<code>s</code>); the sum of these is <code><em>157</em></code>.</p>
<p>Find the item type that appears in both compartments of each rucksack. <em>What is the sum of the priorities of those item types?</em></p>
</article>

<article class="day-desc"><h2 id="part2">Part 2</h2><p>As you finish identifying the misplaced items, the Elves come to you with another issue.</p>
<p>For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the <em>only item type carried by all three Elves</em>. That is, if a group's badge is item type <code>B</code>, then all three Elves will have item type <code>B</code> somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.</p>
<p>The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.</p>
<p>Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is <em>common between all three Elves</em> in each group.</p>
<p>Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:</p>
<pre><code>vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
</code></pre>
<p>And the second group's rucksacks are the next three lines:</p>
<pre><code>wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
</code></pre>
<p>In the first group, the only item type that appears in all three rucksacks is lowercase <code>r</code>; this must be their badges. In the second group, their badge item type must be <code>Z</code>.</p>
<p>Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (<code>r</code>) for the first group and 52 (<code>Z</code>) for the second group. The sum of these is <code><em>70</em></code>.</p>
<p>Find the item type that corresponds to the badges of each three-Elf group. <em>What is the sum of the priorities of those item types?</em></p>
</article>
</details>

<details close>
<summary>Day 4: Camp Cleanup</summary>
<article class="day-desc"><h2>Part 1</h2><p>Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique <em>ID number</em>, and each Elf is assigned a range of section IDs.</p>
<p>However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments <em>overlap</em>. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a <em>big list of the section assignments for each pair</em> (your puzzle input).</p>
<p>For example, consider the following list of section assignment pairs:</p>
<pre><code>2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
</code></pre>
<p>For the first few pairs, this list means:</p>
<ul>
<li>Within the first pair of Elves, the first Elf was assigned sections <code>2-4</code> (sections <code>2</code>, <code>3</code>, and <code>4</code>), while the second Elf was assigned sections <code>6-8</code> (sections <code>6</code>, <code>7</code>, <code>8</code>).</li>
<li>The Elves in the second pair were each assigned two sections.</li>
<li>The Elves in the third pair were each assigned three sections: one got sections <code>5</code>, <code>6</code>, and <code>7</code>, while the other also got <code>7</code>, plus <code>8</code> and <code>9</code>.</li>
</ul>
<p>This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:</p>
<pre><code>.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
</code></pre>
<p>Some of the pairs have noticed that one of their assignments <em>fully contains</em> the other. For example, <code>2-8</code> fully contains <code>3-7</code>, and <code>6-6</code> is fully contained by <code>4-6</code>. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are <code><em>2</em></code> such pairs.</p>
<p><em>In how many assignment pairs does one range fully contain the other?</em></p>
</article>

<article class="day-desc"><h2 id="part2">Part 2</h2><p>It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would <span title="If you like this, you'll *love* axis-aligned bounding box intersection testing.">like</span> to know the number of pairs that <em>overlap at all</em>.</p>
<p>In the above example, the first two pairs (<code>2-4,6-8</code> and <code>2-3,4-5</code>) don't overlap, while the remaining four pairs (<code>5-7,7-9</code>, <code>2-8,3-7</code>, <code>6-6,4-6</code>, and <code>2-6,4-8</code>) do overlap:</p>
<ul>
<li><code>5-7,7-9</code> overlaps in a single section, <code>7</code>.</li>
<li><code>2-8,3-7</code> overlaps all of the sections <code>3</code> through <code>7</code>.</li>
<li><code>6-6,4-6</code> overlaps in a single section, <code>6</code>.</li>
<li><code>2-6,4-8</code> overlaps in sections <code>4</code>, <code>5</code>, and <code>6</code>.</li>
</ul>
<p>So, in this example, the number of overlapping assignment pairs is <code><em>4</em></code>.</p>
<p><em>In how many assignment pairs do the ranges overlap?</em></p>
</article>
</details>

<details close>
<summary>Day 5: Supply Stacks</summary>
<article class="day-desc"><h2>Part 1</h2><p>The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked <em>crates</em>, but because the needed supplies are buried under many other crates, the crates need to be rearranged.</p>
<p>The ship has a <em>giant cargo crane</em> capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.</p>
<p>The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her <em>which</em> crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.</p>
<p>They do, however, have a drawing of the starting stacks of crates <em>and</em> the rearrangement procedure (your puzzle input). For example:</p>
<pre><code>    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
</code></pre>
<p>In this example, there are three stacks of crates. Stack 1 contains two crates: crate <code>Z</code> is on the bottom, and crate <code>N</code> is on top. Stack 2 contains three crates; from bottom to top, they are crates <code>M</code>, <code>C</code>, and <code>D</code>. Finally, stack 3 contains a single crate, <code>P</code>.</p>
<p>Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:</p>
<pre><code>[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
</code></pre>
<p>In the second step, three crates are moved from stack 1 to stack 3. Crates are moved <em>one at a time</em>, so the first crate to be moved (<code>D</code>) ends up below the second and third crates:</p>
<pre><code>        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
</code></pre>
<p>Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved <em>one at a time</em>, crate <code>C</code> ends up below crate <code>M</code>:</p>
<pre><code>        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
</code></pre>
<p>Finally, one crate is moved from stack 1 to stack 2:</p>
<pre><code>        [<em>Z</em>]
        [N]
        [D]
[<em>C</em>] [<em>M</em>] [P]
 1   2   3
</code></pre>
<p>The Elves just need to know <em>which crate will end up on top of each stack</em>; in this example, the top crates are <code>C</code> in stack 1, <code>M</code> in stack 2, and <code>Z</code> in stack 3, so you should combine these together and give the Elves the message <code><em>CMZ</em></code>.</p>
<p><em>After the rearrangement procedure completes, what crate ends up on top of each stack?</em></p>
</article>

<article class="day-desc"><h2 id="part2">Part 2</h2><p>As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.</p>
<p>Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a <em><span title="It's way better than the old CrateMover 1006.">CrateMover 9001</span></em>.</p>
<p>The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and <em>the ability to pick up and move multiple crates at once</em>.</p>
<p>Again considering the example above, the crates begin in the same configuration:</p>
<pre><code>    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
</code></pre>
<p>Moving a single crate from stack 2 to stack 1 behaves the same as before:</p>
<pre><code>[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
</code></pre>
<p>However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates <em>stay in the same order</em>, resulting in this new configuration:</p>
<pre><code>        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
</code></pre>
<p>Next, as both crates are moved from stack 2 to stack 1, they <em>retain their order</em> as well:</p>
<pre><code>        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
</code></pre>
<p>Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate <code>C</code> that gets moved:</p>
<pre><code>        [<em>D</em>]
        [N]
        [Z]
[<em>M</em>] [<em>C</em>] [P]
 1   2   3
</code></pre>
<p>In this example, the CrateMover 9001 has put the crates in a totally different order: <code><em>MCD</em></code>.</p>
<p>Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. <em>After the rearrangement procedure completes, what crate ends up on top of each stack?</em></p>
</article>
</details>

<details close>
<summary>Day 6: Tuning Trouble</summary>
<article class="day-desc"><h2>Part 1</h2><p>The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the <em class="star">star</em> fruit grove.</p>
<p>As you move through the dense undergrowth, one of the Elves gives you a handheld <em>device</em>. He says that it has many fancy features, but the most important one to set up right now is the <em>communication system</em>.</p>
<p>However, because he's heard you have <a href="/2016/day/6">significant</a> <a href="/2016/day/25">experience</a> <a href="/2019/day/7">dealing</a> <a href="/2019/day/9">with</a> <a href="/2019/day/16">signal-based</a> <a href="/2021/day/25">systems</a>, he convinced the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.</p>
<p>As if inspired by comedic timing, the device emits a few <span title="The magic smoke, on the other hand, seems to be contained... FOR NOW!">colorful sparks</span>.</p>
<p>To be able to communicate with the Elves, the device needs to <em>lock on to their signal</em>. The signal is a series of seemingly-random characters that the device receives one at a time.</p>
<p>To fix the communication system, you need to add a subroutine to the device that detects a <em>start-of-packet marker</em> in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of <em>four characters that are all different</em>.</p>
<p>The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify the first position where the four most recently received characters were all different. Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.</p>
<p>For example, suppose you receive the following datastream buffer:</p>
<pre><code>mjqjpqmgbljsphdztnvjfqwrcgsmlb</code></pre>
<p>After the first three characters (<code>mjq</code>) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters <code>mjqj</code>. Because <code>j</code> is repeated, this isn't a marker.</p>
<p>The first time a marker appears is after the <em>seventh</em> character arrives. Once it does, the last four characters received are <code>jpqm</code>, which are all different. In this case, your subroutine should report the value <code><em>7</em></code>, because the first start-of-packet marker is complete after 7 characters have been processed.</p>
<p>Here are a few more examples:</p>
<ul>
<li><code>bvwbjplbgvbhsrlpgdmjqwftvncz</code>: first marker after character <code><em>5</em></code></li>
<li><code>nppdvjthqldpwncqszvftbrmjlhg</code>: first marker after character <code><em>6</em></code></li>
<li><code>nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg</code>: first marker after character <code><em>10</em></code></li>
<li><code>zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw</code>: first marker after character <code><em>11</em></code></li>
</ul>
<p><em>How many characters need to be processed before the first start-of-packet marker is detected?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for <em>messages</em>.</p>
<p>A <em>start-of-message marker</em> is just like a start-of-packet marker, except it consists of <em>14 distinct characters</em> rather than 4.</p>
<p>Here are the first positions of start-of-message markers for all of the above examples:</p>
<ul>
<li><code>mjqjpqmgbljsphdztnvjfqwrcgsmlb</code>: first marker after character <code><em>19</em></code></li>
<li><code>bvwbjplbgvbhsrlpgdmjqwftvncz</code>: first marker after character <code><em>23</em></code></li>
<li><code>nppdvjthqldpwncqszvftbrmjlhg</code>: first marker after character <code><em>23</em></code></li>
<li><code>nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg</code>: first marker after character <code><em>29</em></code></li>
<li><code>zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw</code>: first marker after character <code><em>26</em></code></li>
</ul>
<p><em>How many characters need to be processed before the first start-of-message marker is detected?</em></p>
</article>

</details>

<details close>
<summary>Day 7: No Space Left On Device</summary>
<article class="day-desc"><h2>Part 1</h2><p>You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?</p>
<p>The device the Elves gave you has problems with more than just its communication system. You try to run a system update:</p>
<pre><code>$ system-update --please --pretty-please-with-sugar-on-top
<span title="E099 PROGRAMMER IS OVERLY POLITE">Error</span>: No space left on device
</code></pre>
<p>Perhaps you can delete some files to make space for the update?</p>
<p>You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:</p>
<pre><code>$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
</code></pre>
<p>The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called <code>/</code>. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.</p>
<p>Within the terminal output, lines that begin with <code>$</code> are <em>commands you executed</em>, very much like some modern computers:</p>
<ul>
<li><code>cd</code> means <em>change directory</em>. This changes which directory is the current directory, but the specific result depends on the argument:
  <ul>
  <li><code>cd x</code> moves <em>in</em> one level: it looks in the current directory for the directory named <code>x</code> and makes it the current directory.</li>
  <li><code>cd ..</code> moves <em>out</em> one level: it finds the directory that contains the current directory, then makes that directory the current directory.</li>
  <li><code>cd /</code> switches the current directory to the outermost directory, <code>/</code>.</li>
  </ul>
</li>
<li><code>ls</code> means <em>list</em>. It prints out all of the files and directories immediately contained by the current directory:
  <ul>
  <li><code>123 abc</code> means that the current directory contains a file named <code>abc</code> with size <code>123</code>.</li>
  <li><code>dir xyz</code> means that the current directory contains a directory named <code>xyz</code>.</li>
  </ul>
</li>
</ul>
<p>Given the commands and output in the example above, you can determine that the filesystem looks visually like this:</p>
<pre><code>- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
</code></pre>
<p>Here, there are four directories: <code>/</code> (the outermost directory), <code>a</code> and <code>d</code> (which are in <code>/</code>), and <code>e</code> (which is in <code>a</code>). These directories also contain files of various sizes.</p>
<p>Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the <em>total size</em> of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)</p>
<p>The total sizes of the directories above can be found as follows:</p>
<ul>
<li>The total size of directory <code>e</code> is <em>584</em> because it contains a single file <code>i</code> of size 584 and no other directories.</li>
<li>The directory <code>a</code> has total size <em>94853</em> because it contains files <code>f</code> (size 29116), <code>g</code> (size 2557), and <code>h.lst</code> (size 62596), plus file <code>i</code> indirectly (<code>a</code> contains <code>e</code> which contains <code>i</code>).</li>
<li>Directory <code>d</code> has total size <em>24933642</em>.</li>
<li>As the outermost directory, <code>/</code> contains every file. Its total size is <em>48381165</em>, the sum of the size of every file.</li>
</ul>
<p>To begin, find all of the directories with a total size of <em>at most 100000</em>, then calculate the sum of their total sizes. In the example above, these directories are <code>a</code> and <code>e</code>; the sum of their total sizes is <code><em>95437</em></code> (94853 + 584). (As in this example, this process can count files more than once!)</p>
<p>Find all of the directories with a total size of at most 100000. <em>What is the sum of the total sizes of those directories?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>Now, you're ready to choose a directory to delete.</p>
<p>The total disk space available to the filesystem is <code><em>70000000</em></code>. To run the update, you need unused space of at least <code><em>30000000</em></code>. You need to find a directory you can delete that will <em>free up enough space</em> to run the update.</p>
<p>In the example above, the total size of the outermost directory (and thus the total amount of used space) is <code>48381165</code>; this means that the size of the <em>unused</em> space must currently be <code>21618835</code>, which isn't quite the <code>30000000</code> required by the update. Therefore, the update still requires a directory with total size of at least <code>8381165</code> to be deleted before it can run.</p>
<p>To achieve this, you have the following options:</p>
<ul>
<li>Delete directory <code>e</code>, which would increase unused space by <code>584</code>.</li>
<li>Delete directory <code>a</code>, which would increase unused space by <code>94853</code>.</li>
<li>Delete directory <code>d</code>, which would increase unused space by <code>24933642</code>.</li>
<li>Delete directory <code>/</code>, which would increase unused space by <code>48381165</code>.</li>
</ul>
<p>Directories <code>e</code> and <code>a</code> are both too small; deleting them would not free up enough space. However, directories <code>d</code> and <code>/</code> are both big enough! Between these, choose the <em>smallest</em>: <code>d</code>, increasing unused space by <code><em>24933642</em></code>.</p>
<p>Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. <em>What is the total size of that directory?</em></p>
</article>

</details>

[//]: # ()
[//]: # (<details open>)

[//]: # (<summary>Day 8: Task name</summary>)

[//]: # (</details>)

[//]: # ()
[//]: # (<details open>)

[//]: # (<summary>Day 9: Task name</summary>)

[//]: # (</details>)

[//]: # ()
[//]: # (<details open>)

[//]: # (<summary>Day 10: Task name</summary>)

[//]: # (</details>)

[//]: # ()
[//]: # (<details open>)

[//]: # (<summary>Day 11: Task name</summary>)

[//]: # (</details>)

[//]: # ()
[//]: # (<details open>)

[//]: # (<summary>Day 12: Task name</summary>)

[//]: # (</details>)

[//]: # ()
[//]: # (<details open>)

[//]: # (<summary>Day 13: Task name</summary>)

[//]: # (</details>)