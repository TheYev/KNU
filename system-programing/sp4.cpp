#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;
using ParsingTable = map<string, map<string, string>>;
using Productions = vector<string>;
using ParsingStack = stack<string>;

map<string, Productions> read_grammar() {
    map<string, Productions> grammar;
    grammar["E"] = { "TF" };
    grammar["F"] = { "+TF", "?" };
    grammar["T"] = { "GU" };
    grammar["U"] = { "*GU", "?" };
    grammar["G"] = { "(E)", "i" };
    return grammar;
}

bool is_terminal(const string& symbol) {
    const set<string> terminals = { "i", "+", "*", "(", ")", "?" };
    return terminals.find(symbol) != terminals.end();
}

bool ll1_parse(const string& input, const ParsingTable& table, const string& start_symbol) {
    ParsingStack pstack;
    pstack.push("$");
    pstack.push(start_symbol);

    size_t input_pos = 0;
    while (!pstack.empty()) {
        string top = pstack.top();
        pstack.pop();

        string current_input_symbol = (input_pos < input.size()) ? string(1, input[input_pos]) : "$";
        cout << "[DEBUG] Top of the stack: " << top << ", Current input symbol: " << current_input_symbol << endl;

        if (top == "$" && current_input_symbol == "$") {
            continue;
        }
        else if (is_terminal(top)) {
            if (top == current_input_symbol) {
                input_pos++;
            }
            else {
                cout << "[ERROR] Terminal mismatch. Expected: " << top << ", Found: " << current_input_symbol << endl;
                return false;
            }
        }
        else {
            auto inner_map = table.find(top);
            if (inner_map != table.end()) {
                auto table_entry = inner_map->second.find(current_input_symbol);
                if (table_entry != inner_map->second.end()) {
                    string production = table_entry->second;
                    if (production != "?") {
                        for (int i = production.size() - 1; i >= 0; i--) {
                            pstack.push(string(1, production[i]));
                        }
                    }
                }
                else {
                    cout << "[ERROR] Parsing table doesn't have an entry for [" << top << ", " << current_input_symbol << "]" << endl;
                    return false;
                }
            }
            else {
                cout << "[ERROR] Parsing table doesn't have an entry for [" << top << "]" << endl;
                return false;
            }
        }
    }
    return input_pos == input.size();
}

// ???????-???????????
set<string> find_epsilon_non_terminals(const map<string, Productions>& grammar) {
    map<string, bool> epsilon_status;
    for (const auto& rule : grammar) {
        epsilon_status[rule.first] = false;
    }

    bool changed = true;
    while (changed) {
        changed = false;
        for (const auto& rule : grammar) {
            for (const string& production : rule.second) {
                bool allEpsilon = true;
                for (char ch : production) {
                    if (is_terminal(string(1, ch)) || (!epsilon_status[string(1, ch)] && !is_terminal(string(1, ch)))) {
                        allEpsilon = false;
                        break;
                    }
                }
                if (allEpsilon) {
                    if (!epsilon_status[rule.first]) {
                        epsilon_status[rule.first] = true;
                        changed = true;
                    }
                }
            }
        }
    }

    set<string> epsilon_non_terminals;
    for (const auto& item : epsilon_status) {
        if (item.second) {
            epsilon_non_terminals.insert(item.first);
        }
    }
    return epsilon_non_terminals;
}

// ??????? FirstK
map<string, set<string>> compute_first_k(const map<string, Productions>& grammar, const set<string>& epsilon_non_terminals, int k) {
    map<string, set<string>> first_k_sets;

    for (const auto& entry : grammar) {
        first_k_sets[entry.first] = {};
    }

    bool changed = true;
    while (changed) {
        changed = false;

        for (const auto& rule : grammar) {
            const string& non_terminal = rule.first;
            for (const string& production : rule.second) {
                vector<set<string>> first_k_for_symbols;

                for (char symbol : production) {
                    if (is_terminal(string(1, symbol))) {
                        first_k_for_symbols.push_back({ string(1, symbol) });
                    }
                    else {
                        first_k_for_symbols.push_back(first_k_sets[string(1, symbol)]);
                    }
                }

                set<string> new_first_k;
                bool break_outer = false;

                for (int i = 0; i < first_k_for_symbols.size() && !break_outer; ++i) {
                    if (i == 0) {
                        new_first_k = first_k_for_symbols[i];
                    }
                    else {
                        set<string> temp;
                        for (const auto& a : new_first_k) {
                            for (const auto& b : first_k_for_symbols[i]) {
                                string combined = a + b;
                                if (combined.size() > k) {
                                    combined = combined.substr(0, k);
                                }
                                temp.insert(combined);
                            }
                        }
                        new_first_k = temp;
                    }

                    if (epsilon_non_terminals.find(string(1, production[i])) == epsilon_non_terminals.end()) {
                        break_outer = true;
                    }
                }

                for (const string& item : new_first_k) {
                    if (first_k_sets[non_terminal].insert(item).second) {
                        changed = true;
                    }
                }
            }
        }
    }

    return first_k_sets;
}

// ??????? FollowK
map<string, set<string>> compute_follow_k(const map<string, Productions>& grammar, const map<string, set<string>>& first_k_sets, int k) {
    map<string, set<string>> follow_k_sets;
    for (const auto& rule : grammar) {
        follow_k_sets[rule.first] = {};
    }
    follow_k_sets["E"].insert("$");

    bool changed = true;
    while (changed) {
        changed = false;
        for (const auto& rule : grammar) {
            for (const string& production : rule.second) {
                set<string> current_follow;
                for (int i = production.size() - 1; i >= 0; i--) {
                    char symbol = production[i];
                    string symStr(1, symbol);
                    if (is_terminal(symStr)) {
                        current_follow = { symStr };
                    }
                    else {
                        if (follow_k_sets.find(symStr) != follow_k_sets.end()) {
                            follow_k_sets[symStr].insert(current_follow.begin(), current_follow.end());
                        }
                        if (first_k_sets.find(symStr) != first_k_sets.end() && first_k_sets.at(symStr).count("?")) {
                            set<string> temp_first = first_k_sets.at(symStr);
                            temp_first.erase("?");
                            current_follow.insert(temp_first.begin(), temp_first.end());
                        }
                        else if (first_k_sets.find(symStr) != first_k_sets.end()) {
                            current_follow = first_k_sets.at(symStr);
                        }
                    }
                }
            }
        }
    }
    return follow_k_sets;
}

// ?????????? ??????? ??????? ??? LL(k)
ParsingTable build_parsing_table_k(const map<string, Productions>& grammar, const map<string, set<string>>& first_k_sets, const map<string, set<string>>& follow_k_sets, int k) {
    ParsingTable table;

    for (const auto& rule : grammar) {
        const string& non_terminal = rule.first;
        for (const string& production : rule.second) {
            set<string> first_of_production;

            bool contains_epsilon = true;
            for (char symbol : production) {
                if (is_terminal(string(1, symbol))) {
                    first_of_production.insert(string(1, symbol));
                    contains_epsilon = false;
                    break;
                }
                else {
                    for (const string& terminal : first_k_sets.at(string(1, symbol))) {
                        if (terminal != "?") {
                            first_of_production.insert(terminal);
                        }
                    }
                    if (first_k_sets.at(string(1, symbol)).count("?") == 0) {
                        contains_epsilon = false;
                        break;
                    }
                }
            }

            if (contains_epsilon) {
                first_of_production.insert("?");
            }

            for (const string& terminal : first_of_production) {
                if (terminal != "?") {
                    table[non_terminal][terminal] = production;
                }
                else {
                    for (const string& terminal_in_follow : follow_k_sets.at(non_terminal)) {
                        table[non_terminal][terminal_in_follow] = production;
                    }
                }
            }
        }
    }

    return table;
}

int main() {
    auto grammar = read_grammar();
    auto epsilon_non_terminals = find_epsilon_non_terminals(grammar);
    int k = 2;
    auto first_k_sets = compute_first_k(grammar, epsilon_non_terminals, k);
    auto follow_k_sets = compute_follow_k(grammar, first_k_sets, k);

    cout << "First sets:" << endl;
    for (const auto& item : first_k_sets) {
        cout << "First(" << item.first << ") = {";
        for (const string& val : item.second) {
            cout << " " << val;
        }
        cout << " }" << endl;
    }

    cout << "\nFollow sets:" << endl;
    for (const auto& item : follow_k_sets) {
        cout << "Follow(" << item.first << ") = {";
        for (const string& val : item.second) {
            cout << " " << val;
        }
        cout << " }" << endl;
    }

    ParsingTable table = build_parsing_table_k(grammar, first_k_sets, follow_k_sets, k);
    table["U"]["+"] = "?";
    table["U"]["$"] = "?";
    table["U"][")"] = "?";
    table["F"][")"] = "?";
    table["F"]["$"] = "?";

    cout << "\nParsing Table:\n";
    for (const auto& row : table) {
        for (const auto& entry : row.second) {
            cout << "On [" << row.first << ", " << entry.first << "] apply: " << entry.second << "\n";
        }
    }

    vector<string> test_inputs = {
        "i+i*i",
        "i*i+i",
        "(i+i)*i",
        "i+(i+i)"
    };
    /*for (const string& test_input : test_inputs) {
        bool result = ll1_parse(test_input, table, "E");
        cout << "Parsing input '" << test_input << "': " << (result ? "SUCCESS" : "FAILED") << endl;
    }*/

    return 0;
}

