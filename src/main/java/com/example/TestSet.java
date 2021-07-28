package com.example;
import java.io.IOException;
import java.io.InputStream;
import com.fasterxml.jackson.annotation.JsonAutoDetect;

/**
 * Class used for JSON Conversion of GithubAction  Tests
 */
public class TestSet {
    public String repoName;
    public String testName;
    public String dateRun;
    public String numTestsRun;
    public String failures;
    public String errors;
    public String skipped;
    public String timeElapsed;

    public TestSet() {}

    public TestSet(String repoName, String name, String dateRun, String numTestsRun, String failures, String errors, String skipped, String timeElapsed) {
        this.repoName = repoName;
        this.testName = name;
        this.dateRun = dateRun;
        this.numTestsRun = numTestsRun;
        this.failures = failures;
        this.errors = errors;
        this.skipped = skipped;
        this.timeElapsed = timeElapsed;

    }

    public String ToString() {
        return testName + " " + numTestsRun + " " + failures + " " + errors + " " + skipped + " " + timeElapsed;
    }
}