package com.example;
// Import the File class
// Import this class to handle errors
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files
import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;

//hello


public class App 
{
    public static void main( String[] args ) {
        File file = new File("/home/runner/work/cds-javaJson/cds-javaJson/target/surefire-reports/com.example.AppTest.txt");
        //C:\\Users\\VOLYNNX\\cds-GithubActionToPowerBiTest\\target\\surefire-reports\\TicTacTest.txt
        //target\\surefire-reports\\*.txt
        ArrayList<TestSet> tSets = ReadFile(file);
        WriteFile(tSets);
        //hello
         
    }


    private static ArrayList<TestSet> ReadFile(File file) {
      
      String test_set_name = "";
      String tests_run = "";
      String failures = "";
      String errors ="";
      String skipped = "";
      String time_elapsed = "";
      ArrayList<TestSet> tsets = new ArrayList<>();
        try {
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
              String data = scanner.nextLine();
              //System.out.println(data);
              if (data.contains("Test set")) {
                String [] data_split = data.split(":");
                test_set_name = data_split[1].trim();
              } else if (data.contains("Tests run")) {
                String[] data_split = data.split(",");
                for (int i = 0; i < data_split.length; i++) {
                  String [] data_stats = data_split[i].split(":");
                  if (i == 0) {
                     tests_run = data_stats[1].trim();
                  } else if (i == 1) {
                    failures = data_stats[1].trim();
                  } else if (i == 2) {
                    errors = data_stats[1].trim();
                  } else if (i == 3) {
                    skipped = data_stats[1].trim();
                  } else if (i == 4) {
                    time_elapsed = data_stats[1].trim();
                  } 
                }
                System.out.print(System.getenv("Repo_Name"));
                //change enviornment variable to what it is going to be in Github Actions
                String repoName = System.getenv("Repo_Name");
                TestSet ts1 = new TestSet(repoName, test_set_name, tests_run, failures, errors, skipped, time_elapsed);
                tsets.add(ts1);
              }
              
            }
            scanner.close();
            
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
          //TestSet test_Cases = new TestSet(test_set_name, tests_run, failures, errors, skipped, time_elapsed);
          return tsets;
    }

    private static void WriteFile(ArrayList<TestSet> tSets)  {
        //using Jackson
        ObjectMapper objectMapper = new ObjectMapper();
        try {
          objectMapper.writeValue(new File("c:\\_Nikita\\tsting.json"), tSets);
        } catch (JsonGenerationException e) {
          // TODO Auto-generated catch block
          e.printStackTrace();
        } catch (JsonMappingException e) {
          // TODO Auto-generated catch block
          e.printStackTrace();
        } catch (IOException e) {
          // TODO Auto-generated catch block
          e.printStackTrace();
        }
    }
}
