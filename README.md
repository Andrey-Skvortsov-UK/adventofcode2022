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

<details close>
<summary>Day 8: Treetop Tree House</summary>
<article class="day-desc"><h2>Part 1</h2><p>The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a <a href="https://en.wikipedia.org/wiki/Tree_house" target="_blank">tree house</a>.</p>
<p>First, determine whether there is enough tree cover here to keep a tree house <em>hidden</em>. To do this, you need to count the number of trees that are <em>visible from outside the grid</em> when looking directly along a row or column.</p>
<p>The Elves have already launched a <a href="https://en.wikipedia.org/wiki/Quadcopter" target="_blank">quadcopter</a> to generate a map with the height of each tree (<span title="The Elves have already launched a quadcopter (your puzzle input).">your puzzle input</span>). For example:</p>
<pre><code>30373
25512
65332
33549
35390
</code></pre>
<p>Each tree is represented as a single digit whose value is its height, where <code>0</code> is the shortest and <code>9</code> is the tallest.</p>
<p>A tree is <em>visible</em> if all of the other trees between it and an edge of the grid are <em>shorter</em> than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.</p>
<p>All of the trees around the edge of the grid are <em>visible</em> - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the <em>interior nine trees</em> to consider:</p>
<ul>
<li>The top-left <code>5</code> is <em>visible</em> from the left and top. (It isn't visible from the right or bottom since other trees of height <code>5</code> are in the way.)</li>
<li>The top-middle <code>5</code> is <em>visible</em> from the top and right.</li>
<li>The top-right <code>1</code> is not visible from any direction; for it to be visible, there would need to only be trees of height <em>0</em> between it and an edge.</li>
<li>The left-middle <code>5</code> is <em>visible</em>, but only from the right.</li>
<li>The center <code>3</code> is not visible from any direction; for it to be visible, there would need to be only trees of at most height <code>2</code> between it and an edge.</li>
<li>The right-middle <code>3</code> is <em>visible</em> from the right.</li>
<li>In the bottom row, the middle <code>5</code> is <em>visible</em>, but the <code>3</code> and <code>4</code> are not.</li>
</ul>
<p>With 16 trees visible on the edge and another 5 visible in the interior, a total of <code><em>21</em></code> trees are visible in this arrangement.</p>
<p>Consider your map; <em>how many trees are visible from outside the grid?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of <em>trees</em>.</p>
<p>To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)</p>
<p>The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large <a href="https://en.wikipedia.org/wiki/Eaves" target="_blank">eaves</a> to keep it dry, so they wouldn't be able to see higher than the tree house anyway.</p>
<p>In the example above, consider the middle <code>5</code> in the second row:</p>
<pre><code>30373
25<em>5</em>12
65332
33549
35390
</code></pre>
<ul>
<li>Looking up, its view is not blocked; it can see <code><em>1</em></code> tree (of height <code>3</code>).</li>
<li>Looking left, its view is blocked immediately; it can see only <code><em>1</em></code> tree (of height <code>5</code>, right next to it).</li>
<li>Looking right, its view is not blocked; it can see <code><em>2</em></code> trees.</li>
<li>Looking down, its view is blocked eventually; it can see <code><em>2</em></code> trees (one of height <code>3</code>, then the tree of height <code>5</code> that blocks its view).</li>
</ul>
<p>A tree's <em>scenic score</em> is found by <em>multiplying together</em> its viewing distance in each of the four directions. For this tree, this is <code><em>4</em></code> (found by multiplying <code>1 * 1 * 2 * 2</code>).</p>
<p>However, you can do even better: consider the tree of height <code>5</code> in the middle of the fourth row:</p>
<pre><code>30373
25512
65332
33<em>5</em>49
35390
</code></pre>
<ul>
<li>Looking up, its view is blocked at <code><em>2</em></code> trees (by another tree with a height of <code>5</code>).</li>
<li>Looking left, its view is not blocked; it can see <code><em>2</em></code> trees.</li>
<li>Looking down, its view is also not blocked; it can see <code><em>1</em></code> tree.</li>
<li>Looking right, its view is blocked at <code><em>2</em></code> trees (by a massive tree of height <code>9</code>).</li>
</ul>
<p>This tree's scenic score is <code><em>8</em></code> (<code>2 * 2 * 1 * 2</code>); this is the ideal spot for the tree house.</p>
<p>Consider each tree on your map. <em>What is the highest scenic score possible for any tree?</em></p>
</article>
</details>

<details close>
<summary>Day 9: Task name</summary>
<article class="day-desc"><h2>Part 1</h2><p>This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.</p>
<p>It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.</p>
<p>You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where <em>not</em> to step.</p>
<p>Consider a rope with a knot at each end; these knots mark the <em>head</em> and the <em>tail</em> of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.</p>
<p>Due to nebulous reasoning involving <a href="https://en.wikipedia.org/wiki/Planck_units#Planck_length" target="_blank">Planck lengths</a>, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical <em>series of motions</em> (your puzzle input) for the head, you can determine how the tail will move.</p>
<p><span title="I'm an engineer, not a physicist!">Due to the aforementioned Planck lengths</span>, the rope must be quite short; in fact, the head (<code>H</code>) and tail (<code>T</code>) must <em>always be touching</em> (diagonally adjacent and even overlapping both count as touching):</p>
<pre><code>....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...
</code></pre>
<p>If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:</p>
<pre><code>.....    .....    .....
.TH.. -&gt; .T.H. -&gt; ..TH.
.....    .....    .....

...    ...    ...
.T.    .T.    ...
.H. -&gt; ... -&gt; .T.
...    .H.    .H.
...    ...    ...
</code></pre>
<p>Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:</p>
<pre><code>.....    .....    .....
.....    ..H..    ..H..
..H.. -&gt; ..... -&gt; ..T..
.T...    .T...    .....
.....    .....    .....

.....    .....    .....
.....    .....    .....
..H.. -&gt; ...H. -&gt; ..TH.
.T...    .T...    .....
.....    .....    .....
</code></pre>
<p>You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.</p>
<p>For example:</p>
<pre><code>R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
</code></pre>
<p>This series of motions moves the head <em>right</em> four steps, then <em>up</em> four steps, then <em>left</em> three steps, then <em>down</em> one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (<code>s</code> marks the starting position as a reference point):</p>
<pre><code>== Initial State ==

......
......
......
......
H.....  (H covers T, s)

== R 4 ==

......
......
......
......
TH....  (T covers s)

......
......
......
......
sTH...

......
......
......
......
s.TH..

......
......
......
......
s..TH.

== U 4 ==

......
......
......
....H.
s..T..

......
......
....H.
....T.
s.....

......
....H.
....T.
......
s.....

....H.
....T.
......
......
s.....

== L 3 ==

...H..
....T.
......
......
s.....

..HT..
......
......
......
s.....

.HT...
......
......
......
s.....

== D 1 ==

..T...
.H....
......
......
s.....

== R 4 ==

..T...
..H...
......
......
s.....

..T...
...H..
......
......
s.....

......
...TH.
......
......
s.....

......
....TH
......
......
s.....

== D 1 ==

......
....T.
.....H
......
s.....

== L 5 ==

......
....T.
....H.
......
s.....

......
....T.
...H..
......
s.....

......
......
..HT..
......
s.....

......
......
.HT...
......
s.....

......
......
HT....
......
s.....

== R 2 ==

......
......
.H....  (H covers T)
......
s.....

......
......
.TH...
......
s.....
</code></pre>
<p>After simulating the rope, you can count up all of the positions the <em>tail visited at least once</em>. In this diagram, <code>s</code> again marks the starting position (which the tail also visited) and <code>#</code> marks other positions the tail visited:</p>
<pre><code>..##..
...##.
.####.
....#.
s###..
</code></pre>
<p>So, there are <code><em>13</em></code> positions the tail visited at least once.</p>
<p>Simulate your complete hypothetical series of motions. <em>How many positions does the tail of the rope visit at least once?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part Two</h2><p>A rope snaps! Suddenly, the river is getting a lot closer than you remember. The bridge is still there, but some of the ropes that broke are now whipping toward you as you fall through the air!</p>
<p>The ropes are moving too quickly to grab; you only have a few seconds to choose how to arch your body to avoid being hit. Fortunately, your simulation can be extended to support longer ropes.</p>
<p>Rather than two knots, you now must simulate a rope consisting of <em>ten</em> knots. One knot is still the head of the rope and moves according to the series of motions. Each knot further down the rope follows the knot in front of it using the same rules as before.</p>
<p>Using the same series of motions as the above example, but with the knots marked <code>H</code>, <code>1</code>, <code>2</code>, ..., <code>9</code>, the motions now occur as follows:</p>
<pre><code>== Initial State ==

......
......
......
......
H.....  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)

== R 4 ==

......
......
......
......
1H....  (1 covers 2, 3, 4, 5, 6, 7, 8, 9, s)

......
......
......
......
21H...  (2 covers 3, 4, 5, 6, 7, 8, 9, s)

......
......
......
......
321H..  (3 covers 4, 5, 6, 7, 8, 9, s)

......
......
......
......
4321H.  (4 covers 5, 6, 7, 8, 9, s)

== U 4 ==

......
......
......
....H.
4321..  (4 covers 5, 6, 7, 8, 9, s)

......
......
....H.
.4321.
5.....  (5 covers 6, 7, 8, 9, s)

......
....H.
....1.
.432..
5.....  (5 covers 6, 7, 8, 9, s)

....H.
....1.
..432.
.5....
6.....  (6 covers 7, 8, 9, s)

== L 3 ==

...H..
....1.
..432.
.5....
6.....  (6 covers 7, 8, 9, s)

..H1..
...2..
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

.H1...
...2..
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

== D 1 ==

..1...
.H.2..
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

== R 4 ==

..1...
..H2..
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

..1...
...H..  (H covers 2)
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

......
...1H.  (1 covers 2)
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

......
...21H
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

== D 1 ==

......
...21.
..43.H
.5....
6.....  (6 covers 7, 8, 9, s)

== L 5 ==

......
...21.
..43H.
.5....
6.....  (6 covers 7, 8, 9, s)

......
...21.
..4H..  (H covers 3)
.5....
6.....  (6 covers 7, 8, 9, s)

......
...2..
..H1..  (H covers 4; 1 covers 3)
.5....
6.....  (6 covers 7, 8, 9, s)

......
...2..
.H13..  (1 covers 4)
.5....
6.....  (6 covers 7, 8, 9, s)

......
......
H123..  (2 covers 4)
.5....
6.....  (6 covers 7, 8, 9, s)

== R 2 ==

......
......
.H23..  (H covers 1; 2 covers 4)
.5....
6.....  (6 covers 7, 8, 9, s)

......
......
.1H3..  (H covers 2, 4)
.5....
6.....  (6 covers 7, 8, 9, s)
</code></pre>
<p>Now, you need to keep track of the positions the new tail, <code>9</code>, visits. In this example, the tail never moves, and so it only visits <code><em>1</em></code> position. However, <em>be careful</em>: more types of motion are possible than before, so you might want to visually compare your simulated rope to the one above.</p>
<p>Here's a larger example:</p>
<pre><code>R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
</code></pre>
<p>These motions occur as follows (individual steps are not shown):</p>
<pre><code>== Initial State ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........H..............  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)
..........................
..........................
..........................
..........................
..........................

== R 5 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........54321H.........  (5 covers 6, 7, 8, 9, s)
..........................
..........................
..........................
..........................
..........................

== U 8 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
................H.........
................1.........
................2.........
................3.........
...............54.........
..............6...........
.............7............
............8.............
...........9..............  (9 covers s)
..........................
..........................
..........................
..........................
..........................

== L 8 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
........H1234.............
............5.............
............6.............
............7.............
............8.............
............9.............
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
..........................

== D 3 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
.........2345.............
........1...6.............
........H...7.............
............8.............
............9.............
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
..........................

== R 17 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
................987654321H
..........................
..........................
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
..........................

== D 10 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........s.........98765
.........................4
.........................3
.........................2
.........................1
.........................H

== L 25 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
H123456789................

== U 20 ==

H.........................
1.........................
2.........................
3.........................
4.........................
5.........................
6.........................
7.........................
8.........................
9.........................
..........................
..........................
..........................
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
..........................

</code></pre>
<p>Now, the tail (<code>9</code>) visits <code><em>36</em></code> positions (including <code>s</code>) at least once:</p>
<pre><code>..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
#.........................
#.............###.........
#............#...#........
.#..........#.....#.......
..#..........#.....#......
...#........#.......#.....
....#......s.........#....
.....#..............#.....
......#............#......
.......#..........#.......
........#........#........
.........########.........
</code></pre>
<p>Simulate your complete series of motions on a larger rope with ten knots. <em>How many positions does the tail of the rope visit at least once?</em></p>
</article>
</details>

<details close>
<summary>Day 10: Cathode-Ray Tube</summary>
<article class="day-desc"><h2>Part 1</h2><p>You avoid the ropes, plunge into the river, and swim to shore.</p>
<p>The Elves yell something about meeting back up with them upriver, but the river is too loud to tell exactly what they're saying. They finish crossing the bridge and disappear from view.</p>
<p>Situations like this must be why the Elves prioritized getting the communication system on your handheld device working. You pull it out of your pack, but the amount of water slowly draining from a big crack in its screen tells you it probably won't be of much immediate use.</p>
<p><em>Unless</em>, that is, you can design a replacement for the device's video system! It seems to be some kind of <a href="https://en.wikipedia.org/wiki/Cathode-ray_tube" target="_blank">cathode-ray tube</a> screen and simple CPU that are both driven by a precise <em>clock circuit</em>. The clock circuit ticks at a constant rate; each tick is called a <em>cycle</em>.</p>
<p>Start by figuring out the signal being sent by the CPU. The CPU has a single register, <code>X</code>, which starts with the value <code>1</code>. It supports only two instructions:</p>
<ul>
<li><code>addx V</code> takes <em>two cycles</em> to complete. <em>After</em> two cycles, the <code>X</code> register is increased by the value <code>V</code>. (<code>V</code> can be negative.)</li>
<li><code>noop</code> takes <em>one cycle</em> to complete. It has no other effect.</li>
</ul>
<p>The CPU uses these instructions in a program (your puzzle input) to, somehow, tell the screen what to draw.</p>
<p>Consider the following small program:</p>
<pre><code>noop
addx 3
addx -5
</code></pre>
<p>Execution of this program proceeds as follows:</p>
<ul>
<li>At the start of the first cycle, the <code>noop</code> instruction begins execution. During the first cycle, <code>X</code> is <code>1</code>. After the first cycle, the <code>noop</code> instruction finishes execution, doing nothing.</li>
<li>At the start of the second cycle, the <code>addx 3</code> instruction begins execution. During the second cycle, <code>X</code> is still <code>1</code>.</li>
<li>During the third cycle, <code>X</code> is still <code>1</code>. After the third cycle, the <code>addx 3</code> instruction finishes execution, setting <code>X</code> to <code>4</code>.</li>
<li>At the start of the fourth cycle, the <code>addx -5</code> instruction begins execution. During the fourth cycle, <code>X</code> is still <code>4</code>.</li>
<li>During the fifth cycle, <code>X</code> is still <code>4</code>. After the fifth cycle, the <code>addx -5</code> instruction finishes execution, setting <code>X</code> to <code>-1</code>.</li>
</ul>
<p>Maybe you can learn something by looking at the value of the <code>X</code> register throughout execution. For now, consider the <em>signal strength</em> (the cycle number multiplied by the value of the <code>X</code> register) <em>during</em> the 20th cycle and every 40 cycles after that (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).</p>
<p>For example, consider this larger program:</p>
<pre><code>addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
</code></pre>
<p>The interesting signal strengths can be determined as follows:</p>
<ul>
<li>During the 20th cycle, register <code>X</code> has the value <code>21</code>, so the signal strength is 20 * 21 = <em>420</em>. (The 20th cycle occurs in the middle of the second <code>addx -1</code>, so the value of register <code>X</code> is the starting value, <code>1</code>, plus all of the other <code>addx</code> values up to that point: 1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21.)</li>
<li>During the 60th cycle, register <code>X</code> has the value <code>19</code>, so the signal strength is 60 * 19 = <code><em>1140</em></code>.</li>
<li>During the 100th cycle, register <code>X</code> has the value <code>18</code>, so the signal strength is 100 * 18 = <code><em>1800</em></code>.</li>
<li>During the 140th cycle, register <code>X</code> has the value <code>21</code>, so the signal strength is 140 * 21 = <code><em>2940</em></code>.</li>
<li>During the 180th cycle, register <code>X</code> has the value <code>16</code>, so the signal strength is 180 * 16 = <code><em>2880</em></code>.</li>
<li>During the 220th cycle, register <code>X</code> has the value <code>18</code>, so the signal strength is 220 * 18 = <code><em>3960</em></code>.</li>
</ul>
<p>The sum of these signal strengths is <code><em>13140</em></code>.</p>
<p>Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. <em>What is the sum of these six signal strengths?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>It seems like the <code>X</code> register controls the horizontal position of a <a href="https://en.wikipedia.org/wiki/Sprite_(computer_graphics)" target="_blank">sprite</a>. Specifically, the sprite is 3 pixels wide, and the <code>X</code> register sets the horizontal position of the <em>middle</em> of that sprite. (In this system, there is no such thing as "vertical position": if the sprite's horizontal position puts its pixels where the CRT is currently drawing, then those pixels will be drawn.)</p>
<p>You count the pixels on the CRT: 40 wide and 6 high. This CRT screen draws the top row of pixels left-to-right, then the row below that, and so on. The left-most pixel in each row is in position <code>0</code>, and the right-most pixel in each row is in position <code>39</code>.</p>
<p>Like the CPU, the CRT is tied closely to the clock circuit: the CRT draws <em>a single pixel during each cycle</em>. Representing each pixel of the screen as a <code>#</code>, here are the cycles during which the first and last pixel in each row are drawn:</p>
<pre><code>Cycle   1 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle  40
Cycle  41 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle  80
Cycle  81 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle 120
Cycle 121 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle 160
Cycle 161 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle 200
Cycle 201 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle 240
</code></pre>
<p>So, by <a href="https://en.wikipedia.org/wiki/Racing_the_Beam" target="_blank">carefully</a> <a href="https://www.youtube.com/watch?v=sJFnWZH5FXc" target="_blank"><span title="While you're at it, go watch everything else by Retro Game Mechanics Explained, too.">timing</span></a> the CPU instructions and the CRT drawing operations, you should be able to determine whether the sprite is visible the instant each pixel is drawn. If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a <em>lit</em> pixel (<code>#</code>); otherwise, the screen leaves the pixel <em>dark</em> (<code>.</code>).
</p><p>The first few pixels from the larger example above are drawn as follows:</p>
<pre><code>Sprite position: ###.....................................

Start cycle   1: begin executing addx 15
During cycle  1: CRT draws pixel in position 0
Current CRT row: #

During cycle  2: CRT draws pixel in position 1
Current CRT row: ##
End of cycle  2: finish executing addx 15 (Register X is now 16)
Sprite position: ...............###......................

Start cycle   3: begin executing addx -11
During cycle  3: CRT draws pixel in position 2
Current CRT row: ##.

During cycle  4: CRT draws pixel in position 3
Current CRT row: ##..
End of cycle  4: finish executing addx -11 (Register X is now 5)
Sprite position: ....###.................................

Start cycle   5: begin executing addx 6
During cycle  5: CRT draws pixel in position 4
Current CRT row: ##..#

During cycle  6: CRT draws pixel in position 5
Current CRT row: ##..##
End of cycle  6: finish executing addx 6 (Register X is now 11)
Sprite position: ..........###...........................

Start cycle   7: begin executing addx -3
During cycle  7: CRT draws pixel in position 6
Current CRT row: ##..##.

During cycle  8: CRT draws pixel in position 7
Current CRT row: ##..##..
End of cycle  8: finish executing addx -3 (Register X is now 8)
Sprite position: .......###..............................

Start cycle   9: begin executing addx 5
During cycle  9: CRT draws pixel in position 8
Current CRT row: ##..##..#

During cycle 10: CRT draws pixel in position 9
Current CRT row: ##..##..##
End of cycle 10: finish executing addx 5 (Register X is now 13)
Sprite position: ............###.........................

Start cycle  11: begin executing addx -1
During cycle 11: CRT draws pixel in position 10
Current CRT row: ##..##..##.

During cycle 12: CRT draws pixel in position 11
Current CRT row: ##..##..##..
End of cycle 12: finish executing addx -1 (Register X is now 12)
Sprite position: ...........###..........................

Start cycle  13: begin executing addx -8
During cycle 13: CRT draws pixel in position 12
Current CRT row: ##..##..##..#

During cycle 14: CRT draws pixel in position 13
Current CRT row: ##..##..##..##
End of cycle 14: finish executing addx -8 (Register X is now 4)
Sprite position: ...###..................................

Start cycle  15: begin executing addx 13
During cycle 15: CRT draws pixel in position 14
Current CRT row: ##..##..##..##.

During cycle 16: CRT draws pixel in position 15
Current CRT row: ##..##..##..##..
End of cycle 16: finish executing addx 13 (Register X is now 17)
Sprite position: ................###.....................

Start cycle  17: begin executing addx 4
During cycle 17: CRT draws pixel in position 16
Current CRT row: ##..##..##..##..#

During cycle 18: CRT draws pixel in position 17
Current CRT row: ##..##..##..##..##
End of cycle 18: finish executing addx 4 (Register X is now 21)
Sprite position: ....................###.................

Start cycle  19: begin executing noop
During cycle 19: CRT draws pixel in position 18
Current CRT row: ##..##..##..##..##.
End of cycle 19: finish executing noop

Start cycle  20: begin executing addx -1
During cycle 20: CRT draws pixel in position 19
Current CRT row: ##..##..##..##..##..

During cycle 21: CRT draws pixel in position 20
Current CRT row: ##..##..##..##..##..#
End of cycle 21: finish executing addx -1 (Register X is now 20)
Sprite position: ...................###..................
</code></pre>
<p>Allowing the program to run to completion causes the CRT to produce the following image:</p>
<pre><code>##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
</code></pre>
<p>Render the image given by your program. <em>What eight capital letters appear on your CRT?</em></p>
</article>
</details>

<details close>
<summary>Day 11: Monkey in the Middle</summary>
<article class="day-desc"><h2>Part 1</h2><p>As you finally start making your way upriver, you realize your pack is much lighter than you remember. Just then, one of the items from your pack goes flying overhead. Monkeys are playing <a href="https://en.wikipedia.org/wiki/Keep_away" target="_blank">Keep Away</a> with your missing things!</p>
<p>To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation, you realize the monkeys operate based on <em>how worried you are about each item</em>.</p>
<p>You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items, and how the monkey makes decisions based on your worry level. For example:</p>
<pre><code>Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
</code></pre>
<p>Each monkey has several attributes:</p>
<ul>
<li><code>Starting items</code> lists your <em>worry level</em> for each item the monkey is currently holding in the order they will be inspected.</li>
<li><code>Operation</code> shows how your worry level changes as that monkey inspects an item. (An operation like <code>new = old * 5</code> means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)</li>
<li><code>Test</code> shows how the monkey uses your worry level to decide where to throw an item next.
  <ul>
  <li><code>If true</code> shows what happens with an item if the <code>Test</code> was true.</li>
  <li><code>If false</code> shows what happens with an item if the <code>Test</code> was false.</li>
  </ul>
</li>
</ul>
<p>After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item causes your worry level to be <em>divided by three</em> and rounded down to the nearest integer.</p>
<p>The monkeys take turns inspecting and throwing items. On a single monkey's <em>turn</em>, it inspects and throws all of the items it is holding one at a time and in the order listed. Monkey <code>0</code> goes first, then monkey <code>1</code>, and so on until each monkey has had one turn. The process of each monkey taking a single turn is called a <em>round</em>.</p>
<p>When a monkey throws an item to another monkey, the item goes on the <em>end</em> of the recipient monkey's list. A monkey that starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.</p>
<p>In the above example, the first round proceeds as follows:</p>
<pre><code>Monkey 0:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by 19 to 1501.
    Monkey gets bored with item. Worry level is divided by 3 to 500.
    Current worry level is not divisible by 23.
    Item with worry level 500 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 98.
    Worry level is multiplied by 19 to 1862.
    Monkey gets bored with item. Worry level is divided by 3 to 620.
    Current worry level is not divisible by 23.
    Item with worry level 620 is thrown to monkey 3.
Monkey 1:
  Monkey inspects an item with a worry level of 54.
    Worry level increases by 6 to 60.
    Monkey gets bored with item. Worry level is divided by 3 to 20.
    Current worry level is not divisible by 19.
    Item with worry level 20 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 65.
    Worry level increases by 6 to 71.
    Monkey gets bored with item. Worry level is divided by 3 to 23.
    Current worry level is not divisible by 19.
    Item with worry level 23 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 75.
    Worry level increases by 6 to 81.
    Monkey gets bored with item. Worry level is divided by 3 to 27.
    Current worry level is not divisible by 19.
    Item with worry level 27 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 6 to 80.
    Monkey gets bored with item. Worry level is divided by 3 to 26.
    Current worry level is not divisible by 19.
    Item with worry level 26 is thrown to monkey 0.
Monkey 2:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by itself to 6241.
    Monkey gets bored with item. Worry level is divided by 3 to 2080.
    Current worry level is divisible by 13.
    Item with worry level 2080 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 60.
    Worry level is multiplied by itself to 3600.
    Monkey gets bored with item. Worry level is divided by 3 to 1200.
    Current worry level is not divisible by 13.
    Item with worry level 1200 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 97.
    Worry level is multiplied by itself to 9409.
    Monkey gets bored with item. Worry level is divided by 3 to 3136.
    Current worry level is not divisible by 13.
    Item with worry level 3136 is thrown to monkey 3.
Monkey 3:
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 3 to 77.
    Monkey gets bored with item. Worry level is divided by 3 to 25.
    Current worry level is not divisible by 17.
    Item with worry level 25 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 500.
    Worry level increases by 3 to 503.
    Monkey gets bored with item. Worry level is divided by 3 to 167.
    Current worry level is not divisible by 17.
    Item with worry level 167 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 620.
    Worry level increases by 3 to 623.
    Monkey gets bored with item. Worry level is divided by 3 to 207.
    Current worry level is not divisible by 17.
    Item with worry level 207 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 1200.
    Worry level increases by 3 to 1203.
    Monkey gets bored with item. Worry level is divided by 3 to 401.
    Current worry level is not divisible by 17.
    Item with worry level 401 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 3136.
    Worry level increases by 3 to 3139.
    Monkey gets bored with item. Worry level is divided by 3 to 1046.
    Current worry level is not divisible by 17.
    Item with worry level 1046 is thrown to monkey 1.
</code></pre>
<p>After round 1, the monkeys are holding items with these worry levels:</p>
<pre><code>Monkey 0: 20, 23, 27, 26
Monkey 1: 2080, 25, 167, 207, 401, 1046
Monkey 2: 
Monkey 3: 
</code></pre>
<p>Monkeys 2 and 3 aren't holding any items at the end of the round; they both inspected items during the round and threw them all before the round ended.</p>
<p>This process continues for a few more rounds:</p>
<pre><code>After round 2, the monkeys are holding items with these worry levels:
Monkey 0: 695, 10, 71, 135, 350
Monkey 1: 43, 49, 58, 55, 362
Monkey 2: 
Monkey 3: 

After round 3, the monkeys are holding items with these worry levels:
Monkey 0: 16, 18, 21, 20, 122
Monkey 1: 1468, 22, 150, 286, 739
Monkey 2: 
Monkey 3: 

After round 4, the monkeys are holding items with these worry levels:
Monkey 0: 491, 9, 52, 97, 248, 34
Monkey 1: 39, 45, 43, 258
Monkey 2: 
Monkey 3: 

After round 5, the monkeys are holding items with these worry levels:
Monkey 0: 15, 17, 16, 88, 1037
Monkey 1: 20, 110, 205, 524, 72
Monkey 2: 
Monkey 3: 

After round 6, the monkeys are holding items with these worry levels:
Monkey 0: 8, 70, 176, 26, 34
Monkey 1: 481, 32, 36, 186, 2190
Monkey 2: 
Monkey 3: 

After round 7, the monkeys are holding items with these worry levels:
Monkey 0: 162, 12, 14, 64, 732, 17
Monkey 1: 148, 372, 55, 72
Monkey 2: 
Monkey 3: 

After round 8, the monkeys are holding items with these worry levels:
Monkey 0: 51, 126, 20, 26, 136
Monkey 1: 343, 26, 30, 1546, 36
Monkey 2: 
Monkey 3: 

After round 9, the monkeys are holding items with these worry levels:
Monkey 0: 116, 10, 12, 517, 14
Monkey 1: 108, 267, 43, 55, 288
Monkey 2: 
Monkey 3: 

After round 10, the monkeys are holding items with these worry levels:
Monkey 0: 91, 16, 20, 98
Monkey 1: 481, 245, 22, 26, 1092, 30
Monkey 2: 
Monkey 3: 

...

After round 15, the monkeys are holding items with these worry levels:
Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
Monkey 1: 110, 36
Monkey 2: 
Monkey 3: 

...

After round 20, the monkeys are holding items with these worry levels:
Monkey 0: 10, 12, 14, 26, 34
Monkey 1: 245, 93, 53, 199, 115
Monkey 2: 
Monkey 3: 
</code></pre>
<p>Chasing all of the monkeys at once is impossible; you're going to have to focus on the <em>two most active</em> monkeys if you want any hope of getting your stuff back. Count the <em>total number of times each monkey inspects items</em> over 20 rounds:</p>
<pre><code><em>Monkey 0 inspected items 101 times.</em>
Monkey 1 inspected items 95 times.
Monkey 2 inspected items 7 times.
<em>Monkey 3 inspected items 105 times.</em>
</code></pre>
<p>In this example, the two most active monkeys inspected items 101 and 105 times. The level of <em>monkey business</em> in this situation can be found by multiplying these together: <code><em>10605</em></code>.</p>
<p>Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. <em>What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item <em>no longer causes your worry level to be divided by three</em>.</p>
<p>Unfortunately, that relief was all that was keeping your worry levels from reaching <em>ridiculous levels</em>. You'll need to <em>find another way to keep your worry levels manageable</em>.</p>
<p>At this rate, you might be putting up with these monkeys for a <em>very long time</em> - possibly <em><code>10000</code> rounds</em>!</p>
<p>With these new rules, you can still figure out the <span title="Monkey business monkey business monkey business, monkey numbers... is this working?">monkey business</span> after 10000 rounds. Using the same example above:</p>
<pre><code>== After round 1 ==
Monkey 0 inspected items 2 times.
Monkey 1 inspected items 4 times.
Monkey 2 inspected items 3 times.
Monkey 3 inspected items 6 times.

== After round 20 ==
Monkey 0 inspected items 99 times.
Monkey 1 inspected items 97 times.
Monkey 2 inspected items 8 times.
Monkey 3 inspected items 103 times.

== After round 1000 ==
Monkey 0 inspected items 5204 times.
Monkey 1 inspected items 4792 times.
Monkey 2 inspected items 199 times.
Monkey 3 inspected items 5192 times.

== After round 2000 ==
Monkey 0 inspected items 10419 times.
Monkey 1 inspected items 9577 times.
Monkey 2 inspected items 392 times.
Monkey 3 inspected items 10391 times.

== After round 3000 ==
Monkey 0 inspected items 15638 times.
Monkey 1 inspected items 14358 times.
Monkey 2 inspected items 587 times.
Monkey 3 inspected items 15593 times.

== After round 4000 ==
Monkey 0 inspected items 20858 times.
Monkey 1 inspected items 19138 times.
Monkey 2 inspected items 780 times.
Monkey 3 inspected items 20797 times.

== After round 5000 ==
Monkey 0 inspected items 26075 times.
Monkey 1 inspected items 23921 times.
Monkey 2 inspected items 974 times.
Monkey 3 inspected items 26000 times.

== After round 6000 ==
Monkey 0 inspected items 31294 times.
Monkey 1 inspected items 28702 times.
Monkey 2 inspected items 1165 times.
Monkey 3 inspected items 31204 times.

== After round 7000 ==
Monkey 0 inspected items 36508 times.
Monkey 1 inspected items 33488 times.
Monkey 2 inspected items 1360 times.
Monkey 3 inspected items 36400 times.

== After round 8000 ==
Monkey 0 inspected items 41728 times.
Monkey 1 inspected items 38268 times.
Monkey 2 inspected items 1553 times.
Monkey 3 inspected items 41606 times.

== After round 9000 ==
Monkey 0 inspected items 46945 times.
Monkey 1 inspected items 43051 times.
Monkey 2 inspected items 1746 times.
Monkey 3 inspected items 46807 times.

== After round 10000 ==
<em>Monkey 0 inspected items 52166 times.</em>
Monkey 1 inspected items 47830 times.
Monkey 2 inspected items 1938 times.
<em>Monkey 3 inspected items 52013 times.</em>
</code></pre>
<p>After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, the level of <em>monkey business</em> in this situation is now <code><em>2713310158</em></code>.</p>
<p>Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, <em>what is the level of monkey business after 10000 rounds?</em></p>
</article>
</details>

<details close>
<summary>Day 12: Hill Climbing Algorithm</summary>
<article class="day-desc"><h2>Part 1</h2><p>You try contacting the Elves using your <span title="When you look up the specs for your handheld device, every field just says &quot;plot&quot;.">handheld device</span>, but the river you're following must be too low to get a decent signal.</p>
<p>You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where <code>a</code> is the lowest elevation, <code>b</code> is the next-lowest, and so on up to the highest elevation, <code>z</code>.</p>
<p>Also included on the heightmap are marks for your current position (<code>S</code>) and the location that should get the best signal (<code>E</code>). Your current position (<code>S</code>) has elevation <code>a</code>, and the location that should get the best signal (<code>E</code>) has elevation <code>z</code>.</p>
<p>You'd like to reach <code>E</code>, but to save energy, you should do it in <em>as few steps as possible</em>. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be <em>at most one higher</em> than the elevation of your current square; that is, if your current elevation is <code>m</code>, you could step to elevation <code>n</code>, but not to elevation <code>o</code>. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)</p>
<p>For example:</p>
<pre><code><em>S</em>abqponm
abcryxxl
accsz<em>E</em>xk
acctuvwj
abdefghi
</code></pre>
<p>Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the <code>e</code> at the bottom. From there, you can spiral around to the goal:</p>
<pre><code>v..v&lt;&lt;&lt;&lt;
&gt;v.vv&lt;&lt;^
.&gt;vv&gt;E^^
..v&gt;&gt;&gt;^^
..&gt;&gt;&gt;&gt;&gt;^
</code></pre>
<p>In the above diagram, the symbols indicate whether the path exits each square moving up (<code>^</code>), down (<code>v</code>), left (<code>&lt;</code>), or right (<code>&gt;</code>). The location that should get the best signal is still <code>E</code>, and <code>.</code> marks unvisited squares.</p>
<p>This path reaches the goal in <code><em>31</em></code> steps, the fewest possible.</p>
<p><em>What is the fewest steps required to move from your current position to the location that should get the best signal?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.</p>
<p>To maximize exercise while hiking, the trail should start as low as possible: elevation <code>a</code>. The goal is still the square marked <code>E</code>. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from <em>any square at elevation <code>a</code></em> to the square marked <code>E</code>.</p>
<p>Again consider the example from above:</p>
<pre><code><em>S</em>abqponm
abcryxxl
accsz<em>E</em>xk
acctuvwj
abdefghi
</code></pre>
<p>Now, there are six choices for starting position (five marked <code>a</code>, plus the square marked <code>S</code> that counts as being at elevation <code>a</code>). If you start at the bottom-left square, you can reach the goal most quickly:</p>
<pre><code>...v&lt;&lt;&lt;&lt;
...vv&lt;&lt;^
...v&gt;E^^
.&gt;v&gt;&gt;&gt;^^
&gt;^&gt;&gt;&gt;&gt;&gt;^
</code></pre>
<p>This path reaches the goal in only <code><em>29</em></code> steps, the fewest possible.</p>
<p><em>What is the fewest steps required to move starting from any square with elevation <code>a</code> to the location that should get the best signal?</em></p>
</article>
</details>

<details close>
<summary>Day 13: Distress Signal</summary>
<article class="day-desc"><h2>Part 1</h2><p>You climb the hill and again try contacting the Elves. However, you instead receive a signal you weren't expecting: a <em>distress signal</em>.</p>
<p>Your handheld device must still not be working properly; the packets from the distress signal got decoded <em>out of order</em>. You'll need to re-order the list of received packets (your puzzle input) to decode the message.</p>
<p>Your list consists of pairs of packets; pairs are separated by a blank line. You need to identify <em>how many pairs of packets are in the right order</em>.</p>
<p>For example:</p>
<pre><code>[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
</code></pre>
<p><span title="The snailfish called. They want their distress signal back.">Packet data consists of lists and integers.</span> Each list starts with <code>[</code>, ends with <code>]</code>, and contains zero or more comma-separated values (either integers or other lists). Each packet is always a list and appears on its own line.</p>
<p>When comparing two values, the first value is called <em>left</em> and the second value is called <em>right</em>. Then:</p>
<ul>
<li>If <em>both values are integers</em>, the <em>lower integer</em> should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.</li>
<li>If <em>both values are lists</em>, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.</li>
<li>If <em>exactly one value is an integer</em>, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing <code>[0,0,0]</code> and <code>2</code>, convert the right value to <code>[2]</code> (a list containing <code>2</code>); the result is then found by instead comparing <code>[0,0,0]</code> and <code>[2]</code>.</li>
</ul>
<p>Using these rules, you can determine which of the pairs in the example are in the right order:</p>
<pre><code>== Pair 1 ==
- Compare [1,1,3,1,1] vs [1,1,5,1,1]
  - Compare 1 vs 1
  - Compare 1 vs 1
  - Compare 3 vs 5
    - Left side is smaller, so inputs are <em>in the right order</em>

== Pair 2 ==
- Compare [[1],[2,3,4]] vs [[1],4]
  - Compare [1] vs [1]
    - Compare 1 vs 1
  - Compare [2,3,4] vs 4
    - Mixed types; convert right to [4] and retry comparison
    - Compare [2,3,4] vs [4]
      - Compare 2 vs 4
        - Left side is smaller, so inputs are <em>in the right order</em>

== Pair 3 ==
- Compare [9] vs [[8,7,6]]
  - Compare 9 vs [8,7,6]
    - Mixed types; convert left to [9] and retry comparison
    - Compare [9] vs [8,7,6]
      - Compare 9 vs 8
        - Right side is smaller, so inputs are <em>not</em> in the right order

== Pair 4 ==
- Compare [[4,4],4,4] vs [[4,4],4,4,4]
  - Compare [4,4] vs [4,4]
    - Compare 4 vs 4
    - Compare 4 vs 4
  - Compare 4 vs 4
  - Compare 4 vs 4
  - Left side ran out of items, so inputs are <em>in the right order</em>

== Pair 5 ==
- Compare [7,7,7,7] vs [7,7,7]
  - Compare 7 vs 7
  - Compare 7 vs 7
  - Compare 7 vs 7
  - Right side ran out of items, so inputs are <em>not</em> in the right order

== Pair 6 ==
- Compare [] vs [3]
  - Left side ran out of items, so inputs are <em>in the right order</em>

== Pair 7 ==
- Compare [[[]]] vs [[]]
  - Compare [[]] vs []
    - Right side ran out of items, so inputs are <em>not</em> in the right order

== Pair 8 ==
- Compare [1,[2,[3,[4,[5,6,7]]]],8,9] vs [1,[2,[3,[4,[5,6,0]]]],8,9]
  - Compare 1 vs 1
  - Compare [2,[3,[4,[5,6,7]]]] vs [2,[3,[4,[5,6,0]]]]
    - Compare 2 vs 2
    - Compare [3,[4,[5,6,7]]] vs [3,[4,[5,6,0]]]
      - Compare 3 vs 3
      - Compare [4,[5,6,7]] vs [4,[5,6,0]]
        - Compare 4 vs 4
        - Compare [5,6,7] vs [5,6,0]
          - Compare 5 vs 5
          - Compare 6 vs 6
          - Compare 7 vs 0
            - Right side is smaller, so inputs are <em>not</em> in the right order
</code></pre>
<p>What are the indices of the pairs that are already <em>in the right order</em>? (The first pair has index 1, the second pair has index 2, and so on.) In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is <code><em>13</em></code>.</p>
<p>Determine which pairs of packets are already in the right order. <em>What is the sum of the indices of those pairs?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>Now, you just need to put <em>all</em> of the packets in the right order. Disregard the blank lines in your list of received packets.</p>
<p>The distress signal protocol also requires that you include two additional <em>divider packets</em>:</p>
<pre><code>[[2]]
[[6]]
</code></pre>
<p>Using the same rules as before, organize all packets - the ones in your list of received packets as well as the two divider packets - into the correct order.</p>
<p>For the example above, the result of putting the packets in the correct order is:</p>
<pre><code>[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
<em>[[2]]</em>
[3]
[[4,4],4,4]
[[4,4],4,4,4]
<em>[[6]]</em>
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]
</code></pre>
<p>Afterward, locate the divider packets. To find the <em>decoder key</em> for this distress signal, you need to determine the indices of the two divider packets and multiply them together. (The first packet is at index 1, the second packet is at index 2, and so on.) In this example, the divider packets are <em>10th</em> and <em>14th</em>, and so the decoder key is <code><em>140</em></code>.</p>
<p>Organize all of the packets into the correct order. <em>What is the decoder key for the distress signal?</em></p>
</article>
</details>

<details close>
<summary>Day 14: Regolith Reservoir</summary>
<article class="day-desc"><h2>Part 1</h2><p>The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads <em>behind</em> the waterfall.</p>
<p>Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.</p>
<p>As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!</p>
<p>Fortunately, your <a href="/2018/day/17">familiarity</a> with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly <em>air</em> with structures made of <em>rock</em>.</p>
<p>Your scan traces the path of each solid rock structure and reports the <code>x,y</code> coordinates that form the shape of the path, where <code>x</code> represents distance to the right and <code>y</code> represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:</p>
<pre><code>498,4 -&gt; 498,6 -&gt; 496,6
503,4 -&gt; 502,4 -&gt; 502,9 -&gt; 494,9
</code></pre>
<p>This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from <code>498,4</code> through <code>498,6</code> and another line of rock from <code>498,6</code> through <code>496,6</code>.)</p>
<p>The sand is pouring into the cave from point <code>500,0</code>.</p>
<p>Drawing rock as <code>#</code>, air as <code>.</code>, and the source of the sand as <code>+</code>, this becomes:</p>
<pre><code>
  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
</code></pre>
<p>Sand is produced <em>one unit at a time</em>, and the next unit of sand is not produced until the previous unit of sand <em>comes to rest</em>. A unit of sand is large enough to fill one tile of air in your scan.</p>
<p>A unit of sand always falls <em>down one step</em> if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally <em>one step down and to the left</em>. If that tile is blocked, the unit of sand attempts to instead move diagonally <em>one step down and to the right</em>. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand <em>comes to rest</em> and no longer moves, at which point the next unit of sand is created back at the source.</p>
<p>So, drawing sand that has come to rest as <code>o</code>, the first unit of sand simply falls straight down and then stops:</p>
<pre><code>......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......<em>o</em>.#.
#########.
</code></pre>
<p>The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:</p>
<pre><code>......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.
</code></pre>
<p>After a total of five units of sand have come to rest, they form this pattern:</p>
<pre><code>......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.
</code></pre>
<p>After a total of 22 units of sand:</p>
<pre><code>......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.
</code></pre>
<p>Finally, only two more units of sand can possibly come to rest:</p>
<pre><code>......+...
..........
......o...
.....ooo..
....#ooo##
...<em>o</em>#ooo#.
..###ooo#.
....oooo#.
.<em>o</em>.ooooo#.
#########.
</code></pre>
<p>Once all <code><em>24</em></code> units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with <code>~</code>:</p>
<pre><code>.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........
</code></pre>
<p>Using your scan, simulate the falling sand. <em>How many units of sand come to rest before sand starts flowing into the abyss below?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>You realize you misread the scan. There isn't an <span title="Endless Void is my C cover band.">endless void</span> at the bottom of the scan - there's floor, and you're standing on it!</p>
<p>You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a <code>y</code> coordinate equal to <em>two plus the highest <code>y</code> coordinate</em> of any point in your scan.</p>
<p>In the example above, the highest <code>y</code> coordinate of any point is <code>9</code>, and so the floor is at <code>y=11</code>. (This is as if your scan contained one extra rock path like <code>-infinity,11 -&gt; infinity,11</code>.) With the added floor, the example above now looks like this:</p>
<pre><code>        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
&lt;-- etc #################### etc --&gt;
</code></pre>
<p>To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at <code>500,0</code>, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after <code><em>93</em></code> units of sand come to rest:</p>
<pre><code>............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################
</code></pre>
<p>Using your scan, simulate the falling sand until the source of the sand becomes blocked. <em>How many units of sand come to rest?</em></p>
</article>
</details>

<details close>
<summary>Day 15: Beacon Exclusion Zone </summary>
<article class="day-desc"><h2>Part 1</h2><p>You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of deployable <em>sensors</em> that you imagine were originally built to locate lost Elves.</p>
<p>The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.</p>
<p>Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring for the nearest signal source <em>beacon</em>. Sensors and beacons always exist at integer coordinates. Each sensor knows its own position and can <em>determine the position of a beacon precisely</em>; however, sensors can only lock on to the one beacon <em>closest to the sensor</em> as measured by the <a href="https://en.wikipedia.org/wiki/Taxicab_geometry" target="_blank">Manhattan distance</a>. (There is never a tie where two beacons are the same distance to a sensor.)</p>
<p>It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:</p>
<pre><code>Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
</code></pre>
<p>So, consider the sensor at <code>2,18</code>; the closest beacon to it is at <code>-2,15</code>. For the sensor at <code>9,16</code>, the closest beacon to it is at <code>10,16</code>.</p>
<p>Drawing sensors as <code>S</code> and beacons as <code>B</code>, the above arrangement of sensors and beacons looks like this:</p>
<pre><code>               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
</code></pre>
<p>This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at <code>8,7</code>:</p>
<pre><code>               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########<em>S</em>#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....<em>B</em>############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
</code></pre>
<p>This sensor's closest beacon is at <code>2,10</code>, and so you know there are no beacons that close or closer (in any positions marked <code>#</code>).</p>
<p>None of the detected beacons seem to be producing the distress signal, so you'll need to <span title="&quot;When you have eliminated all which is impossible, then whatever remains, however improbable, must be where the missing beacon is.&quot; - Sherlock Holmes">work out</span> where the distress beacon is by working out where it <em>isn't</em>. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.</p>
<p>So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where <code>y=10</code>, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:</p>
<pre><code>                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
<em>10 ..####B######################..</em>
11 .###S#############.###########.
</code></pre>
<p>In this example, in the row where <code>y=10</code>, there are <code><em>26</em></code> positions where a beacon cannot be present.</p>
<p>Consult the report from the sensors you just deployed. <em>In the row where <code>y=2000000</code>, how many positions cannot contain a beacon?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have <code>x</code> and <code>y</code> coordinates each no lower than <code>0</code> and no larger than <code>4000000</code>.</p>
<p>To isolate the distress beacon's signal, you need to determine its <em>tuning frequency</em>, which can be found by multiplying its <code>x</code> coordinate by <code>4000000</code> and then adding its <code>y</code> coordinate.</p>
<p>In the example above, the search space is smaller: instead, the <code>x</code> and <code>y</code> coordinates can each be at most <code>20</code>. With this reduced search area, there is only a single position that could have a beacon: <code>x=14, y=11</code>. The tuning frequency for this distress beacon is <code><em>56000011</em></code>.</p>
<p>Find the only possible position for the distress beacon. <em>What is its tuning frequency?</em></p>
</article>
</details>

<details close>
<summary>Day 16: Proboscidea Volcanium </summary>
<article class="day-desc"><h2>Part 1</h2><p>The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.</p>
<p>The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!</p>
<p>You need to get the elephants out of here, quickly. Your device estimates that you have <em>30 minutes</em> before the volcano erupts, so you don't have time to go back out the way you came in.</p>
<p>You scan the cave for other options and discover a network of pipes and pressure-release <em>valves</em>. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's <em>flow rate</em> if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.</p>
<p>There's even a valve in the room you and the elephants are currently standing in labeled <code>AA</code>. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?</p>
<p>For example, suppose you had the following scan output:</p>
<pre><code>Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
</code></pre>
<p>All of the valves begin <em>closed</em>. You start at valve <code>AA</code>, but it must be damaged or <span title="Wait, sir! The valve, sir! it appears to be... jammed!">jammed</span> or something: its flow rate is <code>0</code>, so there's no point in opening it. However, you could spend one minute moving to valve <code>BB</code> and another minute opening it; doing so would release pressure during the remaining <em>28 minutes</em> at a flow rate of <code>13</code>, a total eventual pressure release of <code>28 * 13 = <em>364</em></code>. Then, you could spend your third minute moving to valve <code>CC</code> and your fourth minute opening it, providing an additional <em>26 minutes</em> of eventual pressure release at a flow rate of <code>2</code>, or <code><em>52</em></code> total pressure released by valve <code>CC</code>.</p>
<p>Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:</p>
<pre><code>== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing <em>20</em> pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing <em>20</em> pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing <em>20</em> pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing <em>33</em> pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing <em>33</em> pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing <em>33</em> pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing <em>33</em> pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing <em>79</em> pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing <em>79</em> pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing <em>79</em> pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
</code></pre>
<p>This approach lets you release the most pressure possible in 30 minutes with this valve layout, <code><em>1651</em></code>.</p>
<p>Work out the steps to release the most pressure in 30 minutes. <em>What is the most pressure you can release?</em></p>
</article>
<article class="day-desc"><h2 id="part2">Part 2</h2><p>You're worried that even with an optimal approach, the pressure released won't be enough. What if you got one of the elephants to help you?</p>
<p>It would take you 4 minutes to teach an elephant how to open the right valves in the right order, leaving you with only <em>26 minutes</em> to actually execute your plan. Would having two of you working together be better, even if it means having less time? (Assume that you teach the elephant before opening any valves yourself, giving you both the same full 26 minutes.)</p>
<p>In the example above, you could teach the elephant to help you as follows:</p>
<pre><code>== Minute 1 ==
No valves are open.
You move to valve II.
The elephant moves to valve DD.

== Minute 2 ==
No valves are open.
You move to valve JJ.
The elephant opens valve DD.

== Minute 3 ==
Valve DD is open, releasing <em>20</em> pressure.
You open valve JJ.
The elephant moves to valve EE.

== Minute 4 ==
Valves DD and JJ are open, releasing <em>41</em> pressure.
You move to valve II.
The elephant moves to valve FF.

== Minute 5 ==
Valves DD and JJ are open, releasing <em>41</em> pressure.
You move to valve AA.
The elephant moves to valve GG.

== Minute 6 ==
Valves DD and JJ are open, releasing <em>41</em> pressure.
You move to valve BB.
The elephant moves to valve HH.

== Minute 7 ==
Valves DD and JJ are open, releasing <em>41</em> pressure.
You open valve BB.
The elephant opens valve HH.

== Minute 8 ==
Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
You move to valve CC.
The elephant moves to valve GG.

== Minute 9 ==
Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
You open valve CC.
The elephant moves to valve FF.

== Minute 10 ==
Valves BB, CC, DD, HH, and JJ are open, releasing <em>78</em> pressure.
The elephant moves to valve EE.

== Minute 11 ==
Valves BB, CC, DD, HH, and JJ are open, releasing <em>78</em> pressure.
The elephant opens valve EE.

(At this point, all valves are open.)

== Minute 12 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.

...

== Minute 20 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.

...

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
</code></pre>
<p>With the elephant helping, after 26 minutes, the best you could do would release a total of <code><em>1707</em></code> pressure.</p>
<p><em>With you and an elephant working together for 26 minutes, what is the most pressure you could release?</em></p>
</article>
</details>

[//]: # ()
[//]: # (<details close>)

[//]: # (<summary>Day 17: Task name</summary>)

[//]: # (</details>)

[//]: # ()
[//]: # (<details close>)

[//]: # (<summary>Day 18: Task name</summary>)

[//]: # (</details>)